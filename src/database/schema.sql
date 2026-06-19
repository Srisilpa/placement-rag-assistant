DROP TABLE IF EXISTS chat_history;
DROP TABLE IF EXISTS question_stats;

CREATE TABLE chat_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255),
    question TEXT NOT NULL,
    answer LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE question_stats (
    question VARCHAR(500) PRIMARY KEY,
    count INT DEFAULT 1,
    last_asked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rag_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    faithfulness FLOAT DEFAULT 0,
    answer_relevancy FLOAT DEFAULT 0,
    context_precision FLOAT DEFAULT 0,
    context_recall FLOAT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);