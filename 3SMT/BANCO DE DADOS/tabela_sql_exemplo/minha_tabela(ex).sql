CREATE TABLE alunos (
    id_aluno INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    matricula VARCHAR(20),
    email VARCHAR(100),
    semestre VARCHAR(10)
);

CREATE TABLE curso (
    id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nome_curso VARCHAR(100),
    nivel VARCHAR(100),
    carga_horaria INT,
    duracao_semestre INT
);

CREATE TABLE disciplina (
    id_disciplina INT PRIMARY KEY AUTO_INCREMENT,
    nome_disciplina VARCHAR(100),
    carga_horaria INT
);

CREATE TABLE professor (
    id_professor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    area_atuacao VARCHAR(50),
    email VARCHAR(100),
    titulacao VARCHAR(50)
);

CREATE TABLE matricula (
    id_matricula INT PRIMARY KEY AUTO_INCREMENT,
    semestre VARCHAR(10),
    ano INT
);

CREATE TABLE notas (
    id_notas INT PRIMARY KEY AUTO_INCREMENT,
    nota_final DECIMAL(5,2),
    frequencia DECIMAL(5,2),
    situacao VARCHAR(20),
    id_matricula INT,
    FOREIGN KEY (id_matricula) REFERENCES matricula (id_matricula)
);

CREATE TABLE pertence_a (
    id_aluno INT,
    id_curso INT,
    FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno),
    FOREIGN KEY (id_curso) REFERENCES curso (id_curso)
);

CREATE TABLE realiza (
    id_aluno INT,
    id_matricula INT,
    FOREIGN KEY (id_aluno) REFERENCES alunos (id_aluno),
    FOREIGN KEY (id_matricula) REFERENCES matricula (id_matricula)
);

CREATE TABLE ligado_a (
    id_curso INT,
    id_disciplina INT,
    FOREIGN KEY (id_curso) REFERENCES curso (id_curso),
    FOREIGN KEY (id_disciplina) REFERENCES disciplina (id_disciplina)
);

CREATE TABLE ministrar (
    id_professor INT,
    id_disciplina INT,
    FOREIGN KEY (id_professor) REFERENCES professor (id_professor),
    FOREIGN KEY (id_disciplina) REFERENCES disciplina (id_disciplina)
);

CREATE TABLE inclui (
    id_disciplina INT,
    id_matricula INT,
    FOREIGN KEY (id_disciplina) REFERENCES disciplina (id_disciplina),
    FOREIGN KEY (id_matricula) REFERENCES matricula (id_matricula)
);