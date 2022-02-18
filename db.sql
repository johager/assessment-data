-- Imagine you are opening a pet adoption agency where you will rescue and care for animals and try to find them owners who are a good match for them.

-- Design a database with at least 4 tables for your pet adoption agency. Include any relationships between tables where you feel they are needed.

-- For example, you’ll need an animals table. Perhaps you have an animal species table as well. The relationship between animal species and animals is one-to-many. For every one species in the species table, you could, at most, have many animals of that species in the animals table.

create table animals (
    id serial primary key,
    animal_type_id int not null references animal_types(id),
    animal_age_id int not null references animal_ages(id),
    name varchar(100) not null,
    is_male boolean not null,
    is_neutered_spayed boolean not null,
    entered timestamp not null default now(),
    adopted timestamp
);

create table animal_types (
    id serial primary key,
    type varchar(50)
);

create table animal_ages (
    id serial primary key,
    age varchar(15)
);

create table owners (
    id serial primary key,
    first_name varchar(75) not null,
    last_name varchar(75) not null,
    animal_is_male boolean,
    animal_is_neutered_spayed boolean,
    created timestamp not null default now()
);

create table owners_animal_types (
    id serial primary key,
    owner_id int not null references owners(id),
    animal_type_id int not null references animal_types(id)
);

create table owners_animal_ages (
    id serial primary key,
    owner_id int not null references owners(id),
    animal_age_id int not null references animal_ages(id)
);

-- required data

insert into ages (age) values
('young'),
('middle-aged'),
('elderly');