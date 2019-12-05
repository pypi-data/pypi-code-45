import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cv2


class Reporter:
    def __init__(self, opt, max_iter):
        self.dir = os.path.join(opt.results_dir, opt.command, opt.exp_name)
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        self.log_name = os.path.join(self.dir, 'loss.txt')
        self.max_iter = max_iter
        if opt.command == 'train':
            with open(self.log_name, 'w') as log_file:
                log_file.write(
                    '==================== Training Loss ====================\n'
                )

    def save_image(self, img, name, cvt=True):
        if cvt:
            img = np.uint8((img[0] + 1.0) * 127.5)
        else:
            img = (img + 1.0) * 127.5
            img = np.uint8(img[0] * 255)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(self.dir, name + '.jpg'), img)

    def save_video(self, img, vw):
        img = np.uint8((img[0] + 1.0) * 127.5)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        vw.write(img)

    def save_loss(self, loss):
        with open(self.log_name, 'a') as log_file:
            log_file.write('%s\n' % loss)

    def save_loss_graph(self):
        log_file = open(self.log_name, 'r')
        _ = log_file.readline()
        lines = log_file.readlines()
        log_file.close()

        epoch, loss_G_A, loss_G_B, loss_D_A, loss_D_B = [], [], [], [], []

        for line in lines:
            e = line[7:line.find(',')]
            itr_s = line.find('iter') + 6
            itr_e = itr_s + line[itr_s:].find(',')
            itr = int(line[itr_s:itr_e]) / self.max_iter
            e = int(e) + itr
            ga_s = line.find('G_A') + 5
            ga_e = ga_s + line[ga_s:].find(',')
            gb_s = line.find('G_B') + 5
            gb_e = gb_s + line[gb_s:].find(',')
            da_s = line.find('D_A') + 5
            da_e = da_s + line[da_s:].find(',')
            db_s = line.find('D_B') + 5

            epoch.append(e)
            loss_G_A.append(float(line[ga_s:ga_e]))
            loss_G_B.append(float(line[gb_s:gb_e]))
            loss_D_A.append(float(line[da_s:da_e]))
            loss_D_B.append(float(line[db_s:-1]))

        plt.suptitle('loss graph', y=0.97, fontsize=20)
        plt.plot(epoch, loss_G_A, color='gold', label='loss_G_A')
        plt.plot(epoch, loss_G_B, color='black', label='loss_G_B')
        plt.plot(epoch, loss_D_A, color='red', label='loss_D_A')
        plt.plot(epoch, loss_D_B, color='blue', label='loss_D_B')
        plt.legend()
        plt.savefig(os.path.join(self.dir, 'loss_graph.jpg'))
        plt.clf()
