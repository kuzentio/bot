#
# SELECT con.contest_id, con.hacker_id, con.name,
#   IFNULL(submission_stat.total_submissions, 0) AS total_submissions,
#   IFNULL(submission_stat.total_accepted_submissions, 0) AS total_accepted_submissions,
#   IFNULL(vs.total_views, 0) AS total_views,
#   IFNULL(vs.total_unique_views, 0) AS total_unique_views
# FROM Contests con
#   LEFT JOIN Colleges col
#     ON con.contest_id = col.contest_id
#   LEFT JOIN Challenges cha
#     ON cha.college_id = col.college_id
#
#
#   LEFT JOIN (
#     SELECT
#       DISTINCT
#       contest.contest_id,
#       SUM(view_stat.total_views) total_views,
#       SUM(view_stat.total_unique_views) total_unique_views
#     FROM View_Stats view_stat
#       LEFT JOIN Challenges challenges
#         ON challenges.challenge_id = view_stat.challenge_id
#       LEFT JOIN Colleges collages
#         ON collages.college_id = challenges.college_id
#       LEFT JOIN Contests contest
#         ON contest.contest_id = collages.contest_id
#
#       GROUP BY
#         contest.contest_id
#
#     ) AS vs
#     ON con.contest_id = vs.contest_id
#
#
#   LEFT JOIN (
#     SELECT
#       DISTINCT
#       contest.contest_id,
#       IFNULL(SUM(sub_stat.total_submissions), 0) total_submissions,
#       IFNULL(SUM(sub_stat.total_accepted_submission), 0) total_accepted_submissions
#     FROM Submission_Stats sub_stat
#       LEFT JOIN Challenges challenges
#         ON challenges.challenge_id = sub_stat.challenge_id
#       LEFT JOIN Colleges collages
#         ON collages.college_id = challenges.college_id
#       LEFT JOIN Contests contest
#         ON contest.contest_id = collages.contest_id
#
#       GROUP BY contest.contest_id
#
#     ) AS submission_stat
#     ON con.contest_id = submission_stat.contest_id
#
# GROUP BY
#   con.contest_id,
#   submission_stat.total_submissions,
#   submission_stat.total_accepted_submissions,
#   vs.total_views,
#   vs.total_unique_views
# HAVING (
#   IFNULL(total_submissions, 0) +
#   IFNULL(total_accepted_submissions, 0) +
#   IFNULL(total_views, 0) +
#   IFNULL(total_unique_views, 0) > 0
# )
#
# ORDER BY con.contest_id


# _____________________________________________________________




SELECT contests.contest_id, contests.hacker_id, contests.name,
  IFNULL(submission_stat.total_submissions, 0) AS total_submissions,
  IFNULL(submission_stat.total_accepted_submissions, 0) AS total_accepted_submissions,
  IFNULL(total_views.total_views, 0) AS total_views,
  IFNULL(total_views.total_unique_views, 0) AS total_unique_views
FROM Contests contests
  LEFT JOIN Colleges colleges
    ON contests.contest_id = colleges.contest_id
  LEFT JOIN Challenges challenges
    ON challenges.college_id = colleges.college_id

  LEFT JOIN (
    SELECT
      DISTINCT
      contest.contest_id,
      SUM(view_stat.total_views) total_views,
      SUM(view_stat.total_unique_views) total_unique_views
    FROM View_Stats view_stat
      LEFT JOIN Challenges challenges
        ON challenges.challenge_id = view_stat.challenge_id
      LEFT JOIN Colleges collages
        ON collages.college_id = challenges.college_id
      LEFT JOIN Contests contest
        ON contest.contest_id = collages.contest_id

      GROUP BY
        contest.contest_id

    ) AS total_views
    ON contests.contest_id = total_views.contest_id

  LEFT JOIN (
    SELECT
      DISTINCT
      contest.contest_id,
      IFNULL(SUM(sub_stat.total_submissions), 0) total_submissions,
      IFNULL(SUM(sub_stat.total_accepted_submission), 0) total_accepted_submissions
    FROM Submission_Stats sub_stat
      LEFT JOIN Challenges challenges
        ON challenges.challenge_id = sub_stat.challenge_id
      LEFT JOIN Colleges collages
        ON collages.college_id = challenges.college_id
      LEFT JOIN Contests contest
        ON contest.contest_id = collages.contest_id

      GROUP BY contest.contest_id

    ) AS submission_stat
    ON contests.contest_id = submission_stat.contest_id

GROUP BY
  contests.contest_id,
  submission_stat.total_submissions,
  submission_stat.total_accepted_submissions,
  total_views.total_views,
  total_views.total_unique_views
HAVING (
  IFNULL(total_submissions, 0) +
  IFNULL(total_accepted_submissions, 0) +
  IFNULL(total_views, 0) +
  IFNULL(total_unique_views, 0) > 0
)

ORDER BY contests.contest_id


# ________________________________________________________________________





