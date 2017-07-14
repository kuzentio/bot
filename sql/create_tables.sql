CREATE TABLE Contests (
  contest_id INT(11) NOT NULL AUTO_INCREMENT,
  hacker_id INT(11) NOT NULL ,
  name varchar(255),
  PRIMARY key(contest_id)
);


CREATE TABLE Colleges(
  college_id INT(11) NOT NULL AUTO_INCREMENT,
  contest_id INT(11) NOT NULL ,
  PRIMARY KEY (college_id),
  FOREIGN KEY(contest_id) REFERENCES Contests(contest_id)
);


CREATE TABLE Challenges(
  challenge_id INT NOT NULL AUTO_INCREMENT,
  college_id INT NOT NULL,
  PRIMARY KEY (challenge_id),
  FOREIGN KEY(college_id) REFERENCES Colleges(college_id)
);


CREATE TABLE View_Stats(
  id INT(11) NOT NULL AUTO_INCREMENT,
  challenge_id INT(11) NOT NULL,
  total_views INT(11),
  total_unique_views INT(11),
  PRIMARY KEY(id),
  FOREIGN KEY(challenge_id) REFERENCES Challenges(challenge_id)
);


CREATE TABLE Submission_Stats(
  id INT(11) NOT NULL AUTO_INCREMENT,
  challenge_id INT(11) NOT NULL,
  total_submissions INT(11),
  total_accepted_submission INT(11),
  PRIMARY KEY(id),
  FOREIGN KEY(challenge_id) REFERENCES Challenges(challenge_id)
);

