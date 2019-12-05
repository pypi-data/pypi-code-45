import tensorflow as tf
from .networks import *
from .imagepool import *
from .model_manager import AbstractModel


class CycleGANModel(AbstractModel):
    def __init__(self, opt, max_iter):
        super(CycleGANModel, self).__init__(opt)

        self.netG_A = Generator(
            'netG_A', nblocks=int(opt.n_blocks_G), upsample=opt.upsample)
        self.nets = ['netG_A']
        self.mode = opt.command
        self.resize = True if opt.load_size != -1 else False

        if self.mode == 'train':
            self.netG_B = Generator(
                'netG_B', nblocks=int(opt.n_blocks_G), upsample=opt.upsample)
            self.netD_A = Discriminator('netD_A', nlayers=int(opt.n_layers_D))
            self.netD_B = Discriminator('netD_B', nlayers=int(opt.n_layers_D))
            self.nets += ['netG_B', 'netD_A', 'netD_B']

            self.lambda_A = float(opt.lambda_A)
            self.lambda_B = float(opt.lambda_B)
            self.lambda_idt = float(opt.lambda_idt)

            self.gen_loss = get_loss_fn(opt.gen_loss)

            self.fake_A_pool = ImagePool(int(opt.pool_size))
            self.fake_B_pool = ImagePool(int(opt.pool_size))

            self.learning_rate = float(opt.learning_rate)
            self.beta1 = float(opt.beta1)

            self.start_decay_step = int(opt.niter) * max_iter
            self.decay_steps = self.start_decay_step + int(
                opt.niter_decay) * max_iter
        else:
            self.is_video = True if opt.video else False
            self.lambda_ab = float(opt.lambda_ab)

    def forward(self):
        # real A -> fake B
        self.fake_B = self.netG_A(self.real_A)
        # real B -> fake A
        self.fake_A = self.netG_B(self.real_B)

        # fake B -> reconstructed A
        self.rec_A = self.netG_B(self.fake_B)
        # fake A -> reconstructed B
        self.rec_B = self.netG_A(self.fake_A)

    def backward_D(self):
        fake_A = self.fake_A_pool.query(self.fake_A)
        fake_B = self.fake_B_pool.query(self.fake_B)

        self.loss_D_A = lsgan_loss_disc(
            self.netD_A(self.real_A), self.netD_A(fake_A))
        self.loss_D_B = lsgan_loss_disc(
            self.netD_B(self.real_B), self.netD_B(fake_B))

    def backward_G(self):
        # Identity loss
        if self.lambda_idt > 0:
            # G_A should be identity if real_B is fed: ||G_A(B) - B||
            self.idt_A = self.netG_A(self.real_B)
            self.loss_idt_A = self.gen_loss(
                self.idt_A, self.real_B) * self.lambda_B * self.lambda_idt

            # G_B should be identity if real_A is fed: ||G_B(A) - A||
            self.idt_B = self.netG_B(self.real_A)
            self.loss_idt_B = self.gen_loss(
                self.idt_B, self.real_A) * self.lambda_A * self.lambda_idt
        else:
            self.loss_idt_A = 0
            self.loss_idt_B = 0

        # GAN loss D_B(G_A(A))
        self.loss_G_A = lsgan_loss_gen(self.netD_B(self.fake_B))
        # Forward cycle loss || G_B(G_A(A)) - A ||
        self.loss_cycle_A = self.gen_loss(self.rec_A,
                                          self.real_A) * self.lambda_A

        # GAN loss D_A(G_B(B))
        self.loss_G_B = lsgan_loss_gen(self.netD_A(self.fake_A))
        # Backward cycle loss || G_A(G_B(B)) - B ||
        self.loss_cycle_B = self.gen_loss(self.rec_B,
                                          self.real_B) * self.lambda_B

        self.loss_G_A += self.loss_cycle_A + self.loss_cycle_B + self.loss_idt_A
        self.loss_G_B += self.loss_cycle_B + self.loss_cycle_A + self.loss_idt_B

    def optimize(self):
        def make_optimizer(loss, variables, name):
            global_step = tf.Variable(
                0, name="%s/global_step" % name, trainable=False)
            starter_learning_rate = self.learning_rate
            end_learning_rate = 0.0

            learning_rate = (tf.where(
                tf.greater_equal(global_step, self.start_decay_step),
                tf.train.polynomial_decay(
                    starter_learning_rate,
                    global_step - self.start_decay_step,
                    self.decay_steps,
                    end_learning_rate,
                    power=1.0), starter_learning_rate))

            with tf.variable_scope(name, reuse=tf.AUTO_REUSE):
                learning_step = (tf.train.AdamOptimizer(
                    learning_rate, beta1=self.beta1).minimize(
                        loss, global_step=global_step, var_list=variables))
            return learning_step

        with tf.variable_scope('optimizers'):
            G_A_opt = make_optimizer(
                self.loss_G_A, self.netG_A.variables, name='Adam_G_A')
            G_B_opt = make_optimizer(
                self.loss_G_B, self.netG_B.variables, name='Adam_G_B')
            D_A_opt = make_optimizer(
                self.loss_D_A, self.netD_A.variables, name='Adam_D_A')
            D_B_opt = make_optimizer(
                self.loss_D_B, self.netD_B.variables, name='Adam_D_B')

        with tf.control_dependencies([G_A_opt, G_B_opt, D_A_opt, D_B_opt]):
            return tf.no_op(name='train_op')

    def get_train_operations(self):
        self.forward()
        self.backward_G()
        self.backward_D()
        optimizers = self.optimize()
        return [
            optimizers, self.loss_G_A, self.loss_G_B, self.loss_D_A,
            self.loss_D_B
        ]

    def get_test_operations(self):
        fake_B = self.netG_A(self.real_A)
        if self.lambda_ab > 0:
            if not (self.resize or self.is_video):
                self.real_A = (self.real_A + 1.0) * 255 - 1.0
            if self.is_video:
                fake_B = ((self.real_A / 127.5) - 1.0
                          ) * self.lambda_ab + fake_B * (1 - self.lambda_ab)
            else:
                fake_B = self.real_A * self.lambda_ab + fake_B * (
                    1 - self.lambda_ab)
        return fake_B

    def get_summary(self):
        images_A = tf.concat([self.real_A, self.fake_B, self.rec_A], 2)
        images_B = tf.concat([self.real_B, self.fake_A, self.rec_B], 2)
        img = tf.concat([images_A, images_B], 1)

        tf.summary.image('image', img, 1)
        tf.summary.scalar('loss_G_A', self.loss_G_A)
        tf.summary.scalar('loss_G_B', self.loss_G_B)
        tf.summary.scalar('loss_D_A', self.loss_D_A)
        tf.summary.scalar('loss_D_B', self.loss_D_B)
        summary = tf.summary.merge_all()

        return img, summary
