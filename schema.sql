DROP TABLE IF EXISTS seed_papers;
DROP TABLE IF EXISTS keywords;
DROP TABLE IF EXISTS topics;

CREATE TABLE topics (
	topic_id SERIAL PRIMARY KEY,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	title TEXT NOT NULL
);

CREATE TABLE seed_papers (
	seed_id SERIAL PRIMARY KEY,
	paper_id TEXT NOT NULL,
	topic_id INTEGER NOT NULL,
	CONSTRAINT fk_topic
		FOREIGN KEY (topic_id)
                	REFERENCES topics (topic_id)
);

CREATE TABLE keywords (
	keyword_id SERIAL PRIMARY KEY,
	keyword TEXT NOT NULL,
	topic_id INTEGER NOT NULL,
	CONSTRAINT fk_topic
		FOREIGN KEY (topic_id)
                	REFERENCES topics (topic_id)
);
