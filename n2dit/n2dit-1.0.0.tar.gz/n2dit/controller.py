try:
    import signal
    import os
    from .option_manager import OptionManager
    from .logger import Logger
    from .model_manager import ModelManager
    from .dataset_loader import DatasetLoader
except ImportError as error:
    print(error)
    exit()


class Controller():
    def __init__(self):
        self.stop_operations = []

    def run(self):
        try:
            signal.signal(signal.SIGINT, self._abrupt_terminate_handler)
            opt = OptionManager.parse()
            logger = Logger.init(
                "Controller",
                "INFO",
                log_file=os.path.join(
                    opt.results_dir, "logs",
                    "n2dit_" + opt.command + "_" + opt.exp_name + ".log"))
            Logger.info("Controller",
                        "config: " + str(opt)[len("Namespace("):-1])
            #TODO: Add video dataset load with method of DatasetLoader
            if hasattr(opt, 'video') and opt.video != None:
                Logger.info("Controller", "Using Video Input")
                model_manager = ModelManager(opt)
            else:
                Logger.info("Controller", "Dataset Loading Start")
                dataset_loader = DatasetLoader(opt)
                Logger.info("Controller", "Dataset Loading End")
                model_manager = ModelManager(opt, len(dataset_loader))
            model_manager.setup()
            self.stop_operations.append(model_manager.stop)

            Logger.info("Controller", opt.command + " Start")
            if opt.command == 'train':
                model_manager.train(dataset_loader)
            elif opt.command == 'test':
                if opt.video:
                    model_manager.test()
                else:
                    model_manager.test(dataset_loader)
            else:
                Logger.error("Controller", "ERROR Command: " + opt.command)
            Logger.info("Controller", opt.command + " End")

        except Exception as e:
            Logger.error("Controller", str(e))
            exit()

    def _abrupt_terminate_handler(self, signum, frame):
        Logger.error("Controller", "Forced shutdown")
        if not self.stop_operations:
            quit()
        for operation in self.stop_operations:
            operation()
