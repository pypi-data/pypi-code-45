import argparse
from datetime import datetime
from .version import __version__
import configparser


class OptionManager():
    """
    This class
    """

    def __init__():
        pass

    @staticmethod
    def parse():
        '''
        parse function
        '''
        parser = argparse.ArgumentParser(
            prog=__package__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument(
            '-v', '--version', action='version', version=__version__)
        model_parser = parser.add_subparsers(dest='model')
        model_parser_dict = {}

        ### CycleGAN Options
        cyclegan_model_parser = model_parser.add_parser(
            'cyclegan', help='CycleGAN Model')
        cyclegan_subparsers = cyclegan_model_parser.add_subparsers(
            dest='command')
        cyclegan_train_parser = cyclegan_subparsers.add_parser(
            'train', help='Training mode')
        OptionManager._cyclegan_train_option(cyclegan_train_parser)
        cyclegan_test_parser = cyclegan_subparsers.add_parser(
            'test', help='Test mode')
        OptionManager._cyclegan_test_option(cyclegan_test_parser)
        model_parser_dict["cyclegan"] = {}
        model_parser_dict["cyclegan"]["model"] = cyclegan_model_parser
        model_parser_dict["cyclegan"]["train"] = cyclegan_train_parser
        model_parser_dict["cyclegan"]["test"] = cyclegan_test_parser
        ###

        args = parser.parse_args()
        if len(vars(args)) <= 1:
            parser.print_help()
            quit()
        if args.command is None:
            model_parser_dict[args.model]["model"].print_help()
            quit()
        if args.config_file:
            cfg_file_opt = OptionManager._parse_cfg_file(
                args.config_file, args.model)
            cfg_file_opt_str = "--" + " --".join(
                ("{} {}".format(opt, val)
                 for opt, val in cfg_file_opt.items()))
            args_ = model_parser_dict[args.model][args.command].parse_args(
                cfg_file_opt_str.split())
            diffkeys = [
                k for k in args_.__dict__
                if args_.__dict__[k] != args.__dict__[k]
            ]
            for k in diffkeys:
                if k != "config_file":
                    setattr(args, k, args_.__dict__[k])
        return args

    @staticmethod
    def _cyclegan_train_option(parser):
        parser.add_argument(
            '-C',
            '--config_file',
            type=str,
            help='Config file to load options.')
        parser.add_argument(
            '-A',
            '--dirA',
            type=str,
            help='Domain A image directory path for training datasets.')
        parser.add_argument(
            '-B',
            '--dirB',
            type=str,
            help='Domain B image directory path for training datasets.')
        parser.add_argument(
            '-rd',
            '--results_dir',
            type=str,
            default='./results',
            help=
            'Irectory path where training results are stored. default=./results'
        )
        parser.add_argument(
            '-ls',
            '--load_size',
            type=int,
            default=286,
            help=
            'Scale images to this size. Specifying -1 does not scale. default=286'
        )
        parser.add_argument(
            '-cs',
            '--crop_size',
            type=int,
            default=256,
            help='Crop to this size. Specifying -1 does not crop. default=256')
        parser.add_argument(
            '-ch',
            '--channels',
            type=int,
            default=3,
            help=
            '# of input image channels. 3 for RGB and 1 for grayscale. default=3'
        )
        parser.add_argument(
            '--shuffle',
            default="yes",
            nargs='?',
            type=str,
            help='Shuffle datasets.')
        parser.add_argument(
            '-ps',
            '--pool_size',
            type=int,
            default=50,
            help=
            'Size of image buffer that stores previously generated images. default=50'
        )
        parser.add_argument(
            '-en',
            '--exp_name',
            type=str,
            default=datetime.now().strftime('%Y%m%d_%H%M'),
            help=
            'Identifier of the experiment you want to train. If not specified, it is named <year><month><day>_<hour><minute>. ex)20191201_0326'
        )
        parser.add_argument(
            '--continue',
            dest='continue_',
            default="no",
            nargs='?',
            type=str,
            help=
            'Continue training the latest model corresponding to the experiment name. default=no'
        )
        parser.add_argument(
            '-ep',
            '--epoch',
            type=int,
            default=0,
            help=
            'Starting epoch count. Use it if you want to continue training from a specific epoch while using the continue option. Only the last five epochs are available. default=0'
        )
        parser.add_argument(
            '-n',
            '--niter',
            type=int,
            default=100,
            help='# of iteration at starting learning rate. default=100')
        parser.add_argument(
            '-nd',
            '--niter_decay',
            type=int,
            default=100,
            help=
            '# of iteration to linearly decay learning rate to zero. default=100'
        )
        parser.add_argument(
            '-dlf',
            '--disp_loss_freq',
            type=int,
            default=10,
            help='Iteration cycle to print losses. default=10')
        parser.add_argument(
            '-dsf',
            '--disp_summary_freq',
            type=int,
            default=100,
            help=
            'Iteration cycle to generate loss graphs and intermediate result images. default=100'
        )
        parser.add_argument(
            '-lr',
            '--learning_rate',
            type=float,
            default=0.0002,
            help='Initial learning rate for adam. default=0.0002')
        parser.add_argument(
            '-b1',
            '--beta1',
            type=float,
            default=0.5,
            help='Momentum term of adam. default=0.5')
        parser.add_argument(
            '-lA',
            '--lambda_A',
            type=float,
            default=10.0,
            help=
            'Weight for cycle-consistency loss (A -> B\' -> A\'). default=10.0'
        )
        parser.add_argument(
            '-lB',
            '--lambda_B',
            type=float,
            default=10.0,
            help=
            'Weight for cycle-consistency loss (B -> A\' -> B\'). default=10.0'
        )
        parser.add_argument(
            '-li',
            '--lambda_idt',
            type=float,
            default=0.5,
            help=
            'Use identity mapping. Setting lambda_idt other than 0 has an effect of scaling the weight of the identity mapping loss. For example, if the weight of the identity loss should be 10 times smaller than the weight of the reconstruction loss, please set lambda_identity to 0.1.'
        )
        parser.add_argument(
            '-gm',
            '--gan_mode',
            type=str,
            default='lsgan',
            help='Type of GAN objective. default=lsgan')
        parser.add_argument(
            '-us',
            '--upsample',
            type=str,
            default='trans_conv',
            help='Type of upsampling on Generator. default=trans_conv')
        parser.add_argument(
            '-gl',
            '--gen_loss',
            type=str,
            default='l1',
            help=
            'Type of loss function on Generator. "l1" for l1 loss and "pcpt" for perceptual loss. default=l1'
        )
        parser.add_argument(
            '-nbg',
            '--n_blocks_G',
            type=int,
            default=9,
            help='Number of Resnet blocks in Generator. default=9')
        parser.add_argument(
            '-nld',
            '--n_layers_D',
            type=int,
            default=4,
            help=
            'Number of encoding layers in Discriminator. If less than 3, it is set to 3. default=4'
        )

    @staticmethod
    def _cyclegan_test_option(parser):
        group = parser.add_mutually_exclusive_group()
        parser.add_argument(
            '-C',
            '--config_file',
            type=str,
            help='Config file to load options.')
        group.add_argument(
            '-A',
            '--dirA',
            type=str,
            help='Domain A image directory path for test datasets.')
        group.add_argument(
            '-V',
            '--video',
            type=str,
            help='Video file path for test datasets.')
        parser.add_argument(
            '-rd',
            '--results_dir',
            type=str,
            default='./results',
            help=
            'Results directory path used for training, test results are saved in "[Results Directory]/test/[Experiment Name]/" directory. default=./results'
        )
        parser.add_argument(
            '-ls',
            '--load_size',
            type=int,
            default=-1,
            help=
            'Scale images to this size. Specifying -1 does not scale. default=-1'
        )
        parser.add_argument(
            '-ch',
            '--channels',
            type=int,
            default=3,
            help=
            '# of input image channels. 3 for RGB and 1 for grayscale. default=3'
        )
        parser.add_argument(
            '-lab',
            '--lambda_ab',
            type=float,
            default=0.8,
            help='Weight for alpha blending. default=0.8')
        parser.add_argument(
            '-ep',
            '--epoch',
            type=int,
            default=0,
            help=
            'Number of epoch to be loaded. default=0 which means the latest')
        parser.add_argument(
            '-en',
            '--exp_name',
            type=str,
            help='Experiment identifier used for training.')
        parser.add_argument(
            '-us',
            '--upsample',
            type=str,
            default='trans_conv',
            help=
            'Type of upsampling on Generator. "trans_conv" and "resize_conv" are available. default=trans_conv'
        )
        parser.add_argument(
            '-nbg',
            '--n_blocks_G',
            type=int,
            default=9,
            help='Number of Resnet blocks in Generator. default=9')

    @staticmethod
    def _parse_cfg_file(cfg_file_path, model):
        with open(cfg_file_path, 'r') as f:
            config_string = f.read()
        config = configparser.ConfigParser()
        config.optionxform = lambda option: option
        config.read_string(config_string)
        return config[model]
