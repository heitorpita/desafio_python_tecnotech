CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    data_ingresso DATE NOT NULL
);


CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    carga_horaria INTEGER NOT NULL,
    valor_inscricao DECIMAL(10, 2) NOT NULL,
    status BOOLEAN DEFAULT TRUE 
);

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    data_matricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(10) DEFAULT 'PENDENTE', 
    
    CONSTRAINT fk_aluno FOREIGN KEY (aluno_id) REFERENCES alunos (id) ON DELETE CASCADE,
    CONSTRAINT fk_curso FOREIGN KEY (curso_id) REFERENCES cursos (id) ON DELETE RESTRICT
);

-- 4. Inserções de Teste (Seed Data)
INSERT INTO alunos (nome, email, cpf, data_ingresso) VALUES 
('João Silva', 'joao@email.com', '111.222.333-44', '2025-01-10'),
('Maria Souza', 'maria@email.com', '555.666.777-88', '2025-02-15');

INSERT INTO cursos (nome, carga_horaria, valor_inscricao, status) VALUES 
('Python Fullstack', 40, 1200.00, TRUE),
('Docker Mastery', 10, 300.50, TRUE);

INSERT INTO matriculas (aluno_id, curso_id, status) VALUES 
(1, 1, 'PAGO'),
(1, 2, 'PENDENTE'),
(2, 1, 'PENDENTE');