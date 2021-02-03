print('\033[1;34;40m{:^145}'.format('UEFA CHAMPIONS LEAGUE'))

# import group_stage
# qualified_teams = group_stage.group_stage()

qualified_teams = [
  {'winner': 1, 'runner-up': 0}, {'winner': 4, 'runner-up': 5}, {'winner': 8, 'runner-up': 9}, {'winner': 13, 'runner-up': 12},
  {'winner': 17, 'runner-up': 19}, {'winner': 20, 'runner-up': 21}, {'winner': 25, 'runner-up': 24}, {'winner': 31, 'runner-up': 29}]
import knockout_phase
knockout_phase.knockout_phase(qualified_teams)

# import common_test
# common_test.add_results_test()