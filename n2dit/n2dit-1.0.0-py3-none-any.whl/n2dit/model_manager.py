import os
from abc import *
import cv2
import numpy as np
import tensorflow as tf
from .reporter import Reporter
from .logger import Logger


class AbstractModel(metaclass=ABCMeta):
    def __init__(self, opt):
        self.real_A = tf.placeholder(
            tf.float32, shape=[1, None, None, opt.channels], name='real_A')
        self.real_B = tf.placeholder(
            tf.float32, shape=[1, None, None, opt.channels], name='real_B')

    @abstractmethod
    def get_train_operations(self):
        pass

    @abstractmethod
    def get_test_operations(self):
        pass

    def get_placeholders(self):
        return self.real_A, self.real_B

    @abstractmethod
    def get_summary(self):
        pass


def get_model(model=None):
    if model == "cyclegan":
        from .cycle_gan_model import CycleGANModel
        return CycleGANModel
    else:
        return None


class ModelManager:
    def __init__(self, opt, max_iter=0):
        self._stop = False
        self.mode = opt.command
        self._checkpoints_dir = os.path.join(opt.results_dir, 'train',
                                             opt.exp_name, 'checkpoints')
        self._max_iter = int(max_iter)
        self.epoch = int(opt.epoch)
        self.model = get_model("cyclegan")(opt, self._max_iter)
        self.reporter = Reporter(opt, self._max_iter)
        self.resize = True if opt.load_size != -1 else False
        self.results_dir = opt.results_dir

        if self.mode == 'train':
            self._train_continue = opt.continue_ == 'yes'
            self._max_epoch = opt.niter + opt.niter_decay
            self.loss_freq = opt.disp_loss_freq
            self.summary_freq = opt.disp_summary_freq
        else:
            self.is_video = True if opt.video else False
            if self.is_video:
                self.video = opt.video
                self.video_resize = opt.load_size
                self.outputs_dir = os.path.join(opt.results_dir, 'test',
                                                opt.exp_name)

    def setup(self):
        self.real_A, self.real_B = self.model.get_placeholders()
        if self.mode == "train":
            self._tf_ops = self.model.get_train_operations()
            self.summary = self.model.get_summary()
            self.iter_len = len(str(self._max_epoch * self._max_iter))
        else:
            self._tf_ops = self.model.get_test_operations()

        self.save_paths = dict(
            zip(self.model.nets, [
                os.path.join(self._checkpoints_dir, net)
                for net in self.model.nets
            ]))

        if self.mode == "train":
            self.savers = dict(
                zip(self.model.nets, [
                    tf.train.Saver(
                        tf.get_collection(
                            tf.GraphKeys.GLOBAL_VARIABLES, scope=net))
                    for net in self.model.nets
                ]))

            self.save_paths['optimizers'] = os.path.join(
                self._checkpoints_dir, 'optimizers')
            self.savers['optimizers'] = tf.train.Saver(
                tf.get_collection(
                    tf.GraphKeys.GLOBAL_VARIABLES, scope='optimizers'))

    def train(self, dataset_loader):
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(tf.local_variables_initializer())

            real_A, real_B = dataset_loader.get_next()
            if self._train_continue:
                self._load_checkpoint(sess)
            writer = tf.summary.FileWriter(os.path.join(self.results_dir, "logs"), sess.graph)

            for epoch in range(self.epoch + 1, self._max_epoch + 1):
                for itr in range(1, self._max_iter + 1):
                    if self._stop:
                        break
                    real_A_val, real_B_val = sess.run([real_A, real_B])
                    _, loss_G_A, loss_G_B, loss_D_A, loss_D_B = (sess.run(
                        self._tf_ops,
                        feed_dict={
                            self.real_A: real_A_val,
                            self.real_B: real_B_val
                        }))

                    total_cnt = (epoch - 1) * self._max_iter + itr

                    if total_cnt % self.loss_freq == 0:
                        loss = "epoch: %d, iter: %d, loss_G_A: %f, loss_G_B: %f, loss_D_A: %f, loss_D_B: %f" %\
                                (epoch, itr, loss_G_A, loss_G_B, loss_D_A, loss_D_B)
                        Logger.info("ModelManager", loss)
                        self.reporter.save_loss(loss)

                    if total_cnt % self.summary_freq == 0:
                        img, summary = sess.run(
                            self.summary,
                            feed_dict={
                                self.real_A: real_A_val,
                                self.real_B: real_B_val
                            })

                        self.reporter.save_image(
                            img, 'iter' + str(total_cnt).zfill(self.iter_len))
                        Logger.info("ModelManager",
                                    "The image has been saved: " + 'iter' +
                                    str(total_cnt).zfill(self.iter_len))
                        self.reporter.save_loss_graph()
                        writer.add_summary(summary, total_cnt)
                        writer.flush()
                if self._stop:
                    break
                self._save_checkpoint(sess, epoch)
                Logger.info(
                    "ModelManager",
                    "The checkpoint has been saved: " + 'epoch%d' % epoch)

    def test(self, dataset_loader=None):
        # generate fake images
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(tf.local_variables_initializer())
            self.savers = {'netG_A': tf.train.Saver()}

            self._load_checkpoint(sess)
            if self.is_video:
                cap = cv2.VideoCapture(self.video)
                fourcc = cv2.VideoWriter_fourcc(*'MJPG')

                if self.resize:
                    width = self.video_resize
                    height = self.video_resize
                else:
                    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                vw = cv2.VideoWriter(
                    os.path.join(self.outputs_dir, 'fake.avi'), fourcc,
                    cap.get(cv2.CAP_PROP_FPS), (width, height))

                total_cnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                while (cap.isOpened()):
                    ret, frame = cap.read()
                    if self._stop or not ret:
                        break
                    if self.resize:
                        frame = cv2.resize(
                            frame,
                            dsize=(width, height),
                            interpolation=cv2.INTER_AREA)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = np.expand_dims(frame, 0)
                    fake = sess.run(
                        self._tf_ops, feed_dict={
                            self.real_A: frame
                        })
                    self.reporter.save_video(fake, vw)
                    frm_cnt = cap.get(cv2.CAP_PROP_POS_FRAMES)
                    if frm_cnt % 5 == 0 or frm_cnt == total_cnt:
                        Logger.info("ModelManager", 'processing video: %d/%d' %
                                    (frm_cnt, total_cnt))
                cap.release()
                vw.release()
            else:
                real = dataset_loader.get_next()
                for itr in range(1, self._max_iter + 1):
                    if self._stop:
                        break
                    real_val = sess.run([real])[0]
                    fake = sess.run(
                        self._tf_ops, feed_dict={
                            self.real_A: real_val
                        })

                    self.reporter.save_image(
                        real_val,
                        'real_' + str(itr).zfill(len(str(self._max_iter))),
                        self.resize)
                    self.reporter.save_image(
                        fake,
                        'fake_' + str(itr).zfill(len(str(self._max_iter))))

                    if itr % 5 == 0:
                        Logger.info("ModelManager", 'processing image: %d/%d' %
                                    (itr, self._max_iter))

    def stop(self):
        self._stop = True

    def _load_checkpoint(self, sess):
        def _restore_sess(sess, checkpoint_path):
            try:
                saver.restore(sess, checkpoint_path)
            except ValueError:
                Logger.error(
                    "ModelManager",
                    "Failed to restore variables from checkpoints. The checkpoints file does not exist or is invalid."
                )
                raise Exception("Terminated due to an error.")
            except tf.errors.NotFoundError:
                Logger.error(
                    "ModelManager",
                    "Failed to restore variables from checkpoints. Please check the network settings."
                )
                raise Exception("Terminated due to an error.")

        if self.epoch != 0:
            for net_name in self.model.nets:
                save_path = self.save_paths[net_name]
                saver = self.savers[net_name]
                _restore_sess(sess, "%s/%s-%d" % (save_path, net_name,
                                                  self.epoch))
            checkpoint_file = None
        else:
            for net_name in self.model.nets:
                save_path = self.save_paths[net_name]
                saver = self.savers[net_name]
                checkpoint_file = tf.train.latest_checkpoint(save_path)
                _restore_sess(sess, checkpoint_file)
            # Update self.epoch to the latest epoch.
            self.epoch = int(checkpoint_file.rsplit('-', 1)[1])

        if self.mode == "train":
            save_path = self.save_paths['optimizers']
            saver = self.savers['optimizers']
            _restore_sess(sess, "%s/%s-%d" % (save_path, 'optimizers',
                                              self.epoch))

    def _save_checkpoint(self, sess, epoch):
        for net_name in self.model.nets:
            save_path = self.save_paths[net_name]
            saver = self.savers[net_name]

            if not os.path.exists(save_path):
                os.makedirs(save_path)
            saver.save(sess, os.path.join(save_path, net_name), epoch)

        save_path = self.save_paths['optimizers']
        saver = self.savers['optimizers']
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        saver.save(sess, os.path.join(save_path, 'optimizers'), epoch)
