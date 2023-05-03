-- Active: 1652391343278@@127.0.0.1@5432
CREATE DATABASE tablas;

drop table if exists alumno;
drop table if exists  curso;
drop table if exists docente;
drop table if exists  grupo;
drop table if exists asistencia;

create table usuario (
    id_usuario serial,
    dni varchar(10),
    passw varchar(20),
    nombre varchar(20),
    apellido varchar(20),  
    email varchar(50),
    primary key (id_usuario)
);

--
create table curso (
    id_curso serial,
    id_grupo integer,   
    nombre_curso varchar(50)(20),
    primary key (id_curso)
);

create table tipo_usuario (
    tusr_id integer,
    id_usuario integer,
    nombre_tusr varchar(50), 
    primary key (tusr_id),
	  constraint fk_usuario 
	  foreign key (id_usuario)
    references usuario(id_usuario)
);



create table docente (
    id_docente serial,
    tipo_docente varchar(50),
    curso_docente varchar(50),
    primary key (id_docente)
);

-----------------------------

create table grupo_docente(
	id_docente integer references docente(id_docente),
	id_grupo integer references grupo(id_grupo),
	primary key (id_docente, id_grupo)
);

--------------------------------

create table grupo (
    id_grupo serial,
    id_curso int,
    nombre_grupo varchar(50)(20),
    aula varchar(50)(10),
    primary key (id_grupo),
	  constraint fk_curso
	  foreign key (id_curso)
	  references curso(id_curso)
);
---------------------------------------
----
-----------------------------

create table alumno (
    id_alumno serial,
    alumno_regular boolean,
    alumno_year date,
    primary key (id_alumno)
);

-----------------------
create table horario (
    id_horario serial,
    id_grupo int,
    hora_inicio date,
    hora_fin date,
    dia varchar(50)(20),
    primary key (id_horario),
    constraint fk_grupo
    foreign key (id_grupo)
    references grupo (id_grupo)
);
-------------------------
create table asistencia(
	id_asist serial,
	fecha date,
	id_horario integer,
	id_alumno integer,
	presente bool,
	primary key (id_asist),
	constraint fk_horario
	foreign key (id_horario)
	references horario(id_horario)
);

create table matricula (
	matricula_id serial,
	id_alumno integer,
	id_grupo integer,
	fecha_matricula date,
	estado_matricula varchar(50)(15),
	primary key(matricula_id),
	constraint fk_alumno
	foreign key (id_alumno)
	references alumno(id_alumno),
	constraint fk_grupo
	foreign key (id_grupo)
	references grupo(id_grupo)
);

create table participacion (
    part_id serial,
    part_fecha integer,
    id_horario integer,
    id_alumno integer,
    cantidad integer,
    primary key (part_id),
    constraint fk_horario
    foreign key (id_horario)
    references horario(id_horario)
    
);



create table justificacion(
    id_justif serial,
	id_asist integer,
    fecha date,
    descrip varchar(50)(50),
    primary key (id_justif),
    constraint fk_asistencia
    foreign key (id_asist)
    references asistencia(id_asist)
    
);
select * from usuario;


