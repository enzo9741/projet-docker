CREATE DATABASE IF NOT EXISTS docker;
USE docker;

CREATE TABLE IF NOT EXISTS objects (
    uuid VARCHAR(36),
    brand VARCHAR(36),
    reference VARCHAR(36),
    serial_number VARCHAR(36) ,
    available BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT pk_objects PRIMARY KEY (uuid)
);

/*CREATE TABLE IF NOT EXISTS qrCode (
    id INTEGER AUTO_INCREMENT,
    uuid VARCHAR(36) NOT NULL UNIQUE,

    CONSTRAINT pk_qrCode PRIMARY KEY (id),
    CONSTRAINT fk_qrCode_objects FOREIGN KEY (uuid) REFERENCES objects(uuid) ON DELETE CASCADE
);*/

CREATE TABLE IF NOT EXISTS historic (
    id INT(11) NOT NULL AUTO_INCREMENT,
    uuid VARCHAR(36) NOT NULL,
    date DATETIME,
    old_status VARCHAR(36),
    new_status VARCHAR(36),

    CONSTRAINT pk_historic PRIMARY KEY (id),
    CONSTRAINT fk_historic_objects FOREIGN KEY (uuid) REFERENCES objects(uuid)
);

CREATE TABLE IF NOT EXISTS ram (
    uuid VARCHAR(36),
    capacity VARCHAR(36),
    type VARCHAR(36),
    frequency VARCHAR(36),

    CONSTRAINT pk_ram PRIMARY KEY (uuid),
    CONSTRAINT fk_ram_objects FOREIGN KEY (uuid) REFERENCES objects(uuid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cable (
    uuid VARCHAR(36),
    length VARCHAR(36),
    start_type VARCHAR(36),
    end_type VARCHAR(36),

    CONSTRAINT pk_cable PRIMARY KEY (uuid),
    CONSTRAINT fk_cable_objects FOREIGN KEY (uuid) REFERENCES objects(uuid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cpu (
    uuid VARCHAR(36),
    core TINYINT,
    threads TINYINT,
    frequency VARCHAR(36),

    CONSTRAINT pk_cpu PRIMARY KEY (uuid),
    CONSTRAINT fk_cpu_objects FOREIGN KEY (uuid) REFERENCES objects(uuid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS amovible (
    uuid VARCHAR(36),
    capacity VARCHAR(36),
    tech VARCHAR(36),

    CONSTRAINT pk_amovible PRIMARY KEY (uuid),
    CONSTRAINT fk_amovible_objects FOREIGN KEY (uuid) REFERENCES objects(uuid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS drive (
    uuid VARCHAR(36),
    capacity VARCHAR(36),
    read_value VARCHAR(36),
    write_value VARCHAR(36),

    CONSTRAINT pk_drive PRIMARY KEY (uuid),
    CONSTRAINT fk_drive_objects FOREIGN KEY (uuid) REFERENCES objects(uuid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ssd (
    uuid VARCHAR(36),

    CONSTRAINT pk_ssd PRIMARY KEY (uuid),
    CONSTRAINT fk_ssd_drive FOREIGN KEY (uuid) REFERENCES drive(uuid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS hdd (
    uuid VARCHAR(36),
    rotation_speed VARCHAR(36),
    size VARCHAR(36),

    CONSTRAINT pk_hdd PRIMARY KEY (uuid),
    CONSTRAINT fk_hdd_drive FOREIGN KEY (uuid) REFERENCES drive(uuid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS smart (
    id INT(11) NOT NULL AUTO_INCREMENT,
    startup_number VARCHAR(36),
    power_count VARCHAR(36),
    power_hours VARCHAR(36),
    health_status VARCHAR(36),

    CONSTRAINT pk_smart PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS smart_ssd (
    id INT(11) NOT NULL AUTO_INCREMENT,
    total_read VARCHAR(36),
    total_write VARCHAR(36),

    CONSTRAINT pk_smart_ssd PRIMARY KEY (id),
    CONSTRAINT fk_smart_ssd_smart FOREIGN KEY (id) REFERENCES smart(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS smart_hdd (
    id INT(11) NOT NULL AUTO_INCREMENT,
    faulty_sector VARCHAR(36),

    CONSTRAINT pk_smart_hdd PRIMARY KEY (id),
    CONSTRAINT fk_smart_hdd_smart FOREIGN KEY (id) REFERENCES smart(id) ON DELETE CASCADE
);

-- Create with Github copilot
