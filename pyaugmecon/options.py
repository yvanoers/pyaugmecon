import time
from multiprocessing import cpu_count


class Options(object):
    def __init__(self, opts: dict, solver_opts: dict):
        self.name = opts.get('name', 'Undefined')
        self.gp = opts.get('grid_points')
        self.nadir_p = opts.get('nadir_points')
        self.eps = opts.get('penalty_weight', 1e-3)
        self.round = opts.get('round_decimals', 9)
        self.nadir_r = opts.get('nadir_ratio', 1)
        self.logdir = opts.get('logging_folder', 'logs')
        self.early_exit = opts.get('early_exit', True)
        self.bypass = opts.get('bypass_coefficient', True)
        self.flag = opts.get('flag_array', True)
        self.cpu_count = opts.get('cpu_count', cpu_count())
        self.redivide_work = opts.get('redivide_work', True)
        self.model_fn = opts.get('pickle_file', 'model.p')
        self.shared_flag = opts.get('shared_flag', True)
        self.solver_name = opts.get('solver_name', 'gurobi')
        self.solver_io = opts.get('solver_io', 'python')
        self.output_excel = opts.get('output_excel', True)

        self.solver_opts = solver_opts
        self.solver_opts['MIPGap'] = solver_opts.get('MIPGap', 0.0)
        self.solver_opts['NonConvex'] = solver_opts.get('NonConvex', 2)

        self.time_created = time.strftime("%Y%m%d-%H%M%S")
        self.log_name = self.name + '_' + str(self.time_created)

    def check(self, num_objfun):
        if not self.gp:
            raise Exception('No number of grid points provided')

        if (self.nadir_p and len(self.nadir_p) != num_objfun - 1):
            raise Exception('Too many or too few nadir points provided')
