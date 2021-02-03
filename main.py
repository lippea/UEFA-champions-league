print('\033[1;34;40m{:^145}'.format('UEFA CHAMPIONS LEAGUE'))

import group_stage
qualified_teams = group_stage.group_stage()

import knockout_phase
# knockout_phase.knockout_phase(qualified_teams)

# import common_test
# common_test.add_results_test()