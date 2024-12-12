

CREATE TABLE buses (
    bus_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bus_number TEXT NOT NULL,
    bus_type TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    status TEXT NOT NULL,
    route_id INTEGER NOT NULL,
    route_name TEXT NOT NULL,
    start_location TEXT NOT NULL,
    end_location TEXT NOT NULL
);

CREATE TABLE stops (
    stop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stop_name TEXT NOT NULL,
    location TEXT NOT NULL,
    route_id INTEGER NOT NULL,
    FOREIGN KEY (route_id) REFERENCES routes(route_id)
);


INSERT INTO buses (bus_number, bus_type, capacity, status, route_id, route_name, start_location, end_location)
VALUES 
('101', 'Electric', 40, 'Active', 1,'Kent State to Downtown Kent', 'Kent State University', 'Downtown Kent'),
('102', 'Diesel', 50, 'Active', 2, 'Kent to Akron', 'Kent State University', 'Akron City'),
('103', 'Hybrid', 35, 'Inactive', 3, 'Kent to Ravenna', 'Kent State University', 'Ravenna');

INSERT INTO stops (stop_name, location, route_id)
VALUES 
('Kent State Main Campus', 'Kent State University, Kent, OH', 1),
('Downtown Kent', 'Kent, OH', 1),
('Akron City Center', 'Akron, OH', 2),
('Kent Station', 'Kent, OH', 3),
('Ravenna Downtown', 'Ravenna, OH', 3);

SELECT bus_number, bus_type, status
FROM buses
WHERE route_id = 1;
