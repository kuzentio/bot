CREATE VIEW ContestView AS
  SELECT
    contests.contest_id,
    contests.hacker_id,
    contests.name,
    challenge_id
  FROM
    Contests contests
    LEFT JOIN Colleges colleges
      ON contests.contest_id = colleges.contest_id
    LEFT JOIN Challenges challenges
      ON challenges.college_id = colleges.college_id;

SELECT
  contest_view.contest_id,
  contest_view.hacker_id,
  contest_view.name,
  IFNULL(submissions_stat.total_submission, 0) total_submissions,
  IFNULL(submissions_stat.total_accepted_submission, 0) total_accepted_submissions,
  IFNULL(view_stats.total_view, 0) total_views,
  IFNULL(view_stats.total_unique_view, 0) total_unique_views

FROM ContestView contest_view
  JOIN (
      SELECT
        contest_id,
        SUM(total_views) total_view,
        SUM(total_unique_views) total_unique_view
      FROM ContestView contest_view

        LEFT JOIN View_Stats view_stats
          ON view_stats.challenge_id = contest_view.challenge_id
      GROUP BY contest_view.contest_id
    ) view_stats
  ON
    view_stats.contest_id = contest_view.contest_id
  JOIN (
      SELECT
        contest_id,
        SUM(total_submissions) total_submission,
        SUM(total_accepted_submission) total_accepted_submission
      FROM ContestView contest_view
          LEFT JOIN Submission_Stats submission_stats
            ON submission_stats.challenge_id = contest_view.challenge_id

        GROUP BY contest_view.contest_id
    ) submissions_stat
  ON
    submissions_stat.contest_id = contest_view.contest_id
GROUP BY contest_view.contest_id

HAVING (
  total_submissions + total_accepted_submissions + total_views + total_unique_views > 0
)

