CREATE TABLE IF NOT EXISTS users (

    id SERIAL PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    correo VARCHAR(100) UNIQUE NOT NULL

);

INSERT INTO users(nombre,correo)

VALUES

('Administrador','admin@devops.com')

ON CONFLICT (correo) DO NOTHING;