import initialise
import match
import sort
import finalise
import output

def process_stage(top_32_teams):
  initilised_groups = initialise.random_group(top_32_teams)

  groups_with_points = match.round_robin(initilised_groups)

  groups_with_points_desc = sort.sort_by_points_desc(groups_with_points)

  next_phase_teams_by_group = finalise.get_next_phase_teams(groups_with_points_desc)

  output.print_result(groups_with_points_desc)

  return next_phase_teams_by_group
