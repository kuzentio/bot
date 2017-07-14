

INSERT INTO Contests SET contest_id=66406, hacker_id=17973, name='Rose';
INSERT INTO Contests SET contest_id=66556, hacker_id=79153, name='Angela';
INSERT INTO Contests SET contest_id=94828, hacker_id=80275, name='Frank';


INSERT INTO Colleges SET college_id=11219, contest_id=66406;
INSERT INTO Colleges SET college_id=32473, contest_id=66556;
INSERT INTO Colleges SET college_id=56685, contest_id=94828;


INSERT INTO Challenges SET challenge_id=18765, college_id=11219;
INSERT INTO Challenges SET challenge_id=47127, college_id=11219;
INSERT INTO Challenges SET challenge_id=60292, college_id=32473;
INSERT INTO Challenges SET challenge_id=72974, college_id=56685;


INSERT INTO View_Stats SET challenge_id=47127, total_views=26, total_unique_views=19;
INSERT INTO View_Stats SET challenge_id=47127, total_views=15, total_unique_views=14;
INSERT INTO View_Stats SET challenge_id=18765, total_views=43, total_unique_views=10;
INSERT INTO View_Stats SET challenge_id=18765, total_views=72, total_unique_views=13;
# INSERT INTO View_Stats SET challenge_id=75516, total_views=35, total_unique_views=17;  There is no reference
INSERT INTO View_Stats SET challenge_id=60292, total_views=11, total_unique_views=10;
INSERT INTO View_Stats SET challenge_id=72974, total_views=41, total_unique_views=15;
# INSERT INTO View_Stats SET challenge_id=75516, total_views=75, total_unique_views=11;


# INSERT INTO Submission_Stats SET challenge_id=75516, total_submissions=34, total_accepted_submission=12;
INSERT INTO Submission_Stats SET challenge_id=47127, total_submissions=27, total_accepted_submission=10;
INSERT INTO Submission_Stats SET challenge_id=47127, total_submissions=56, total_accepted_submission=18;
# INSERT INTO Submission_Stats SET challenge_id=75516, total_submissions=74, total_accepted_submission=12;
# INSERT INTO Submission_Stats SET challenge_id=75516, total_submissions=83, total_accepted_submission=8;
INSERT INTO Submission_Stats SET challenge_id=72974, total_submissions=68, total_accepted_submission=24;
INSERT INTO Submission_Stats SET challenge_id=72974, total_submissions=82, total_accepted_submission=14;
INSERT INTO Submission_Stats SET challenge_id=47127, total_submissions=28, total_accepted_submission=11;


