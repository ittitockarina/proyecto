create table farmacia(
    RUC_farm integer primary key,
    nomb_farm varchar(50) not null,
    direc_farm varchar(50) not null,
    telefono integer not null
);
/*
create table usuario (
    id_usuario integer primary key,
    dni varchar(10) unique not null,
    passw varchar(50) not null,
    nombre varchar(50) not null,
    apellido varchar (20) not null,
    RUC_farm integer not null,
    foreign key (RUC_farm)
    	references farmacia(RUC_farm)
);

create table tipo_usuario (
    id_tuser integer not null,
    id_usuario integer not null,
    primary key (id_tuser)
);
*/
create table empleado(
    id_empleado integer primary key,
    nombre_empleado varchar(50) not null,
    apellido_empleado varchar(50) not null,
    direccion_empleado varchar(50) not null,
    cargo varchar(50) not null,
    edad integer not null,
    telefono_empleado varchar(50) not null,
    email_empleado varchar(50),
	RUC_farm integer not null,
    foreign key (RUC_farm)
    	references farmacia(RUC_farm)
);

create table cliente(
    id_cliente integer primary key,
    RUC_cliente integer unique not null,
    nombre_cliente varchar(50) not null,
    direccion_cliente varchar(50) not null,
    telefono_cliente varchar(50) not null,
    RUC_farm integer not null,
    foreign key (RUC_farm)
    	references farmacia(RUC_farm)
);

create table categoria(
    id_categoria integer primary key ,
    nombre_categoria varchar(50) not null,
    description_cat varchar(200)
);

create table presentacion(
    id_presentacion integer primary key,
    nombre_presentacion varchar(50) not null,
    description_pre varchar(200)
);


create table proveedor(
  id_prov integer primary key,
  nombre_prov varchar(50) not null,
  apellido_prov varchar(50) not null,
  direccion_prov varchar(50) not null, 
  telefono_prov varchar(50) not null
);

create table producto(
    id_producto integer primary key,
    nombre_producto varchar(50) not null,
    precio_venta float not null,
    precio_compra float not null,
    stock integer,
    id_presentacion integer not null,
    id_categoria integer not null,
    RUC_farm integer not null,
    id_prov integer not null,
    constraint fk_farmacia
    foreign key (RUC_farm)
    	references farmacia(RUC_farm),
    constraint fk_categoria
    foreign key (id_categoria)
    	references categoria(id_categoria),
    constraint fk_presentacion
    foreign key (id_presentacion)
    	references presentacion(id_presentacion),
    constraint fk_proveedor
    foreign key (id_prov)
    	references proveedor(id_prov)
);


create table tipo_pago(
id_tipo_pago integer primary key,
tipo varchar(50) not null,
emp_tarjeta varchar(50)
);

create table ordenPedido(
  id_ordenPedido integer primary key,
  fecha_pedido date not null,
  id_tipo_pago integer not null,
  id_empleado integer not null,
  id_cliente integer not null,
  constraint fk_empleado
  foreign key (id_empleado) 
  references empleado(id_empleado),
  constraint fk_cliente
  foreign key (id_cliente) 
  references cliente(id_cliente),
  constraint fk_tipo_pago
  foreign key (id_tipo_pago) 
  references tipo_pago(id_tipo_pago)
);


create Table datos_produto (
  id_datos integer primary key,
  id_producto integer not null,
  laboratorio_producto varchar(50) not null,
  ubicacion_producto varchar(50) not null,
  descripcion varchar(50) not null,
  lote varchar(50) not null,
  f_venc date not null,
  constraint fk_producto
  foreign key(id_producto)
  references producto(id_producto)
);


create Table comprobante_pago (
  id_comprobante integer  primary key,
  tipo_comprobante varchar(50) not null,
  fecha_comprobante date not null,
  condicion_pago varchar(50) ,
  plazo_pago varchar(50),
  id_ordenPedido integer not null,
  constraint fk_ordenPedido
  foreign key (id_ordenPedido)
  references ordenPedido(id_ordenPedido)
  --punto_partida varchar,
  --punto_llegada varchar
);

create Table detalle_comprobante (
  id_comprobante integer not null,
  id_datos integer not null,
  p_unit float not null,
  cantidad integer not null,
  descuento float,
  subtotal float not null,
  IGV float,
  total float not null,
  constraint fk_comprobante_pago
  foreign key (id_comprobante)
  references comprobante_pago(id_comprobante),
  constraint fk_datos_produto
  foreign key (id_datos)
  references datos_produto(id_datos)
);
-------------------------------------------------------------------------------------------------------------------------------------------

insert into farmacia (RUC_farm, nomb_farm, direc_farm, telefono) values (215123456789, 'SANNA', 'Av. El fierro 892', 84546552);

insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (1, 21514033670, 'Debera', '2 Blackbird Terrace', '409-298-2581', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (2, 21556292534, 'Laurie', '101 Acker Street', '635-383-5003', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (3, 21546678786, 'Erroll', '07 Morrow Avenue', '466-373-5040', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (4, 21551152431, 'Uriah', '79 Meadow Vale Way', '973-553-6648', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (5, 21535207923, 'Alejandra', '81658 Ridgeway Point', '754-965-5918', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (6, 21579562651, 'Annabal', '0762 Corner Junction', '261-413-5700', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (7, 21583387617, 'Erma', '28962 Hermina Way', '393-952-6026', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (8, 21573096871, 'Rennie', '00 Clarendon Court', '252-415-3696', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (9, 21584536844, 'Cobby', '8 Katie Point', '336-698-6342', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (10, 21556288693, 'Alon', '3 Namekagon Trail', '465-819-1480', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (11, 21515010661, 'Terri', '459 Vahlen Place', '550-638-2457', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (12, 21570761314, 'Griswold', '085 Pepper Wood Pass', '759-575-2088', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (13, 21592205979, 'Andy', '15674 Nova Alley', '475-122-8471', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (14, 21591645704, 'Pam', '5 Gale Circle', '554-730-4561', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (15, 21557923171, 'Giorgio', '45 Bay Park', '223-751-1569', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (16, 21520369702, 'Ranique', '2 Lyons Crossing', '972-926-6361', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (17, 21550300748, 'Michal', '50 Golden Parkway', '604-223-1997', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (18, 21521554930, 'Desi', '37048 Rutledge Pass', '531-220-8249', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (19, 21521678725, 'Tyne', '22 Forest Street', '998-371-8869', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (20, 21553340574, 'George', '436 Kennedy Point', '501-954-7965', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (21, 21591362950, 'Thedric', '95218  Junction', '847-362-5072', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (22, 21514097437, 'Osgood', '9260 Utah Avenue', '649-605-2059', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (23, 21550577816, 'Ellis', '37301 Pond Parkway', '217-367-2325', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (24, 21566115535, 'Onida', '126  Park', '537-361-8917', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (25, 21547956395, 'Kinsley', '075 Stone Drive', '461-838-5830', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (26, 21511681237, 'Novelia', '3 Pearson Park', '156-675-5530', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (27, 21556177978, 'Hugibert', '85506 Darwin Court', '255-870-7723', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (28, 21551752639, 'Egor', '743 Pierstorff Court', '607-966-5686', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (29, 21570728713, 'Nathan', '20 Jenna Parkway', '682-428-3219', 215123456789);
insert into cliente (id_cliente, RUC_cliente, nombre_cliente, direccion_cliente, telefono_cliente, RUC_farm) values (30, 21598652842, 'Rubia', '85 Lien Center', '671-253-5015', 215123456789);

select * from empleado;
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (1, 'Val', 'Pesselt', '0608 Burrows Point', 'caja', 41, '796-473-1722', 'vpesselt0@liveit.ru', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (2, 'Consolata', 'McKiernan', '113 Vermont Park', 'inventario', 45, '806-443-7336', 'cmckiernan1@histats.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (3, 'Wendie', 'Huban', '44199 Spenser Alley', 'RRHH', 42, '302-823-2011', 'whuban2@gizmodo.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (4, 'Gardie', 'Culp', '886 Trailsway Court', 'ventas', 38, '127-327-1824', 'gculp3@blogtalkradio.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (5, 'Enrichetta', 'Scroggs', '57 Quincy Way', 'caja', 40, '164-707-5131', 'escroggs4@slashdot.org', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (6, 'Andrus', 'Dearnaly', '42588 Loomis Pass', 'inventario', 25, '171-538-1031', 'adearnaly5@theglobeandmail.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (7, 'Tine', 'Morena', '24 Acker Circle', 'caja', 39, '957-327-8648', 'tmorenac@example.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (8, 'Torey', 'Thrush', '747 Forest Dale Terrace', 'ventas', 54, '991-484-8393', 'tthrushb@ox.ac.uk', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (9, 'Jany', 'Feaveryear', '9430 Mitchell Park', 'inventario', 46, '247-108-4371', 'jfeaveryeard@yahoo.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (10, 'Horst', 'Woolford', '1 Crescent Oaks Lane', 'RRHH', 44, '845-813-9337', 'hwoolforde@reference.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (11, 'Stormi', 'Fedorchenko', '6 Burrows Avenue', 'ventas', 56, '805-561-7796', 'sfedorchenkof@wufoo.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (12, 'Shelley', 'Maylour', '25438 Saint Paul Crossing', 'caja', 59, '433-902-0235', 'smaylourg@pen.io', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (13, 'Esdras', 'Kivelhan', '420 Prairie Rose Terrace', 'inventario', 32, '517-897-6898', 'ekivelhanh@wiley.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (14, 'Nannette', 'Beste', '758 Pearson Avenue', 'RRHH', 29, '529-236-4230', 'nbestei@hubpages.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (15, 'Ingmar', 'Town', '79092 Goodland Terrace', 'ventas', 37, '978-987-5600', 'itownj@patch.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (16, 'Lillian', 'Cowey', '8 Arkansas Terrace', 'caja', 53, '236-799-4954', 'lcoweyk@nba.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (17, 'Gussy', 'Macvain', '5510 5th Place', 'inventario', 48, '216-863-5506', 'gmacvainl@purevolume.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (18, 'Kurt', 'Goodacre', '767 Mockingbird Crossing', 'RRHH', 56, '877-553-4895', 'kgoodacrem@ebay.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (19, 'Lorne', 'Padginton', '74 Coleman Trail', 'ventas', 63, '427-615-6825', 'lpadgintonn@bandcamp.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (20, 'Marlow', 'Carmont', '51 Marcy Park', 'caja', 61, '895-125-9991', 'mcarmonto@ft.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (21, 'Helena', 'Kobierski', '9 High Crossing Lane', 'inventario', 66, '801-982-6280', 'hkobierskip@blogs.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (22, 'Rozalin', 'Merit', '2317 Transport Avenue', 'RRHH', 42, '250-507-0049', 'rmeritq@bigcartel.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (23, 'Blayne', 'Hulson', '9356 Warbler Terrace', 'ventas', 34, '132-667-6948', 'bhulsonr@jalbum.net', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (24, 'Maude', 'Monshall', '2791 New Castle Avenue', 'caja', 47, '966-415-3598', 'mmonshalls@live.com', 215123456789);
insert into empleado (id_empleado, nombre_empleado, apellido_empleado, direccion_empleado, cargo, edad, telefono_empleado, email_empleado, RUC_farm) values (25, 'Tommy', 'Crudginton', '5 Hazelcrest Crossing', 'inventario', 43, '692-869-5817', 'tcrudgintont@de.vu', 215123456789);

select * from categoria;
insert into categoria (id_categoria, nombre_categoria, description_cat) values (1, 'Productos Farmaceuticos', 'Medicamentos, productos diet\E9ticos, productos biol\F3gicos, productos gal\E9nicos');
insert into categoria (id_categoria, nombre_categoria, description_cat) values (2, 'Dispositivos Medicos', 'De bajo riesgo, medio riesgo, alto riesgo, criticos en materia de riesgo');
insert into categoria (id_categoria, nombre_categoria, description_cat) values (3, 'Productos Sanitario', 'Productos cosmeticos, articulos sanitarios, articulos de limpieza domestica');

select * from presentacion;
insert into presentacion (id_presentacion, nombre_presentacion, description_pre) values (1, 'Caja', 'Encajado');
insert into presentacion (id_presentacion, nombre_presentacion, description_pre) values (2, 'Frasco', 'Enfrascado');
insert into presentacion (id_presentacion, nombre_presentacion, description_pre) values (3, 'Jarabe', 'Embotellado');
insert into presentacion (id_presentacion, nombre_presentacion, description_pre) values (4, 'Paquete', 'Embolsado');
insert into presentacion (id_presentacion, nombre_presentacion, description_pre) values (5, 'blister', 'Muchas Tabletas');

select * from proveedor;
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (1, 'Adelbert', 'Renahan', '52 Stuart Pass', '905-247-9030');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (2, 'Aeriela', 'Trimmell', '51848 Gulseth Court', '671-137-5793');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (3, 'Gale', 'Grise', '278 Esker Crossing', '504-234-8586');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (4, 'Koral', 'Torbard', '314 5th Terrace', '210-283-1460');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (5, 'Merci', 'Beert', '1 Old Shore Way', '206-716-7550');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (6, 'Bartlet', 'Beininck', '912 Mayer Pass', '837-715-6208');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (7, 'Faith', 'Woolvin', '7 South Way', '898-335-5315');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (8, 'Craggie', 'Valentim', '685 3rd Plaza', '496-854-9779');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (9, 'Karmen', 'Boosey', '80 Prentice Plaza', '240-740-5898');
insert into proveedor (id_prov, nombre_prov, apellido_prov, direccion_prov, telefono_prov) values (10, 'Ladonna', 'Laundon', '51 Summerview Pass', '619-913-1749');

select * from producto;
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (1, 'oxycodone hydrochloride', ' 16,12', ' 7,87', 41, 5, 3, 215123456789, 2);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (2, 'ALCOHOL', ' 18,33', ' 7,00', 22, 2, 2, 215123456789, 3);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (3, 'Temozolomide', ' 15,09', ' 6,53', 28, 1, 1, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (4, 'Brewers Yeast', ' 12,69', ' 8,06', 36, 1, 1, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (5, 'Immune Globulin', ' 11,79', ' 9,54', 31, 1, 1, 215123456789, 10);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (6, 'TITANIUM DIOXIDE', ' 13,14', ' 5,31', 16, 3, 1, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (7, 'cephalexin', ' 11,97', ' 7,70', 24, 1, 1, 215123456789, 1);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (8, 'Phenazopyridine HCl', ' 16,20', ' 6,92', 20, 3, 1, 215123456789, 10);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (9, 'Levetiracetam', ' 13,36', ' 7,56', 22, 2, 1, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (10, 'Promethazine Hydrochloride', ' 18,74', ' 7,02', 25, 2, 2, 215123456789, 4);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (11, 'Dexamethasone Intensol', ' 11,06', ' 6,29', 40, 3, 2, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (12, 'ARNICA MONTANA', ' 19,19', ' 9,63', 39, 4, 1, 215123456789, 1);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (13, 'amoxicillina', ' 16,34', ' 9,41', 40, 5, 2, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (14, 'Carbamazepine', ' 16,83', ' 8,17', 40, 1, 2, 215123456789, 2);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (15, 'THYROID, PORCINE', ' 17,25', ' 9,71', 26, 4, 1, 215123456789, 1);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (16, 'Acetaminophen Phenylephrine', ' 12,67', ' 7,73', 16, 5, 2, 215123456789, 8);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (17, 'Isopropyl Alcohol', ' 15,71', ' 8,78', 38, 2, 3, 215123456789, 5);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (18, 'pegvisomant', ' 14,15', ' 5,90', 22, 4, 2, 215123456789, 1);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (19, 'Magnesium hydroxide', ' 13,34', ' 8,33', 17, 3, 1, 215123456789, 8);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (20, 'hydroxyzine pamoate', ' 18,36', ' 8.72', 34, 3, 2, 215123456789, 1);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (21, 'octreotide acetate', ' 14,84', ' 5,41', 37, 3, 1, 215123456789, 10);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (22, 'Atenolol', ' 11,21', ' 9,39', 27, 1, 2, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (23, 'GLYCOPYRROLATE', ' 14,05', ' 6,08', 23, 3, 3, 215123456789, 8);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (24, 'Simethicone', ' 16,34', ' 7,90', 26, 5, 2, 215123456789, 1);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (25, 'hydrochloride', ' 16,00', ' 6,95', 41, 4, 2, 215123456789, 7);
insert into producto (id_producto, nombre_producto, precio_venta, precio_compra, stock, id_presentacion, id_categoria, RUC_farm, id_prov) values (26, 'pioglitazone', ' 16,68', ' 5,18', 26, 1, 3, 215123456789, 2);



insert into tipo_pago (id_tipo_pago, tipo, emp_tarjeta) values (1, 'efectivo', '');
insert into tipo_pago (id_tipo_pago, tipo, emp_tarjeta) values (2, 'tarjeta', 'visa');
insert into tipo_pago (id_tipo_pago, tipo, emp_tarjeta) values (3, 'tarjeta', 'american express');
insert into tipo_pago (id_tipo_pago, tipo, emp_tarjeta) values (4,'tarjeta', 'dinners club');

select * from datos_produto;
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (1, 1, 'Physicians Total Care, Inc.', '812 Pearson Hill', '500 gr', '376082017-4', '24/3/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (2, 2, 'Aphena Pharma Solutions - Tennessee, Inc.', '51 Debra Way', '500 gr', '997048474-5', '29/9/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (3, 3, 'Solbin Co., Ltd', '74409 Morning Drive', '500 gr', '040167000-7', '16/11/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (4, 4, 'Epic Pharma, LLC', '26 Bellgrove Lane', '500 gr', '262752419-4', '7/8/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (5, 5, 'State of Florida DOH Central Pharmacy', '7 Delaware Drive', '500 gr', '059337034-1', '5/11/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (6, 6, 'North Safety Products', '66958 Mockingbird Pass', '500 gr', '935321081-X', '23/6/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (7, 7, 'Rebel Distributors Corp', '54555 Ridgeview Lane', '500 gr', '641857351-X', '21/5/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (8, 8, 'Newton Laboratories, Inc.', '5 Northwestern Plaza', '500 gr', '013249732-8', '22/1/2026');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (9, 9, 'Bath & Body Works, Inc.', '29932 Nova Park', '500 gr', '330472524-5', '28/12/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (10, 10, 'Betco Corporation, Ltd.', '8510 Buena Vista Parkway', '500 gr', '861574506-4', '11/1/2026');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (11, 11, 'CVS Pharmacy', '006 North Hill', '500 gr', '370758211-6', '3/2/2026');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (12, 12, 'HOMEOLAB USA INC.', '73 Bunting Alley', '500 gr', '951309704-8', '3/7/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (13, 13, 'Cardinal Health', '0 Chinook Point', '500 gr', '289425475-X', '20/10/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (14, 14, 'Mylan Pharmaceuticals Inc.', '9253 Sutteridge Court', '500 gr', '207638566-5', '27/5/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (15, 15, 'Nelco Laboratories, Inc.', '6 Roth Drive', '500 gr', '658560176-9', '6/5/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (16, 16, 'Stephen L. LaFrance Pharmacy, Inc.', '77 Bayside Pass', '500 gr', '162114695-2', '26/4/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (17, 17, 'Sandoz Inc', '55148 Lotheville Park', '500 gr', '227774630-4', '25/8/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (18, 18, 'McKesson', '18 Wayridge Alley', '500 gr', '196013295-4', '23/12/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (19, 19, 'Rite Aid Corporation', '888 Hovde Parkway', '500 gr', '286419596-8', '14/9/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (20, 20, 'Bryant Ranch Prepack', '3911 Lyons Place', '500 gr', '379340799-3', '11/10/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (21, 21, 'REMEDYREPACK INC.', '42920 Maywood Crossing', '500 gr', '716972909-1', '12/10/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (22, 22, 'Shire US Manufacturing Inc.', '321 Shelley Center', '500 gr', '879777841-9', '29/9/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (23, 23, 'State of Florida DOH Central Pharmacy', '88 Rieder Lane', '500 gr', '020258955-2', '16/6/2024');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (24, 24, 'McKesson', '0730 Maryland Circle', '500 gr', '890443264-2', '9/12/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (25, 25, 'Stratus Pharmaceuticals', '04063 Toban Circle', '500 gr', '596201085-X', '17/1/2025');
insert into datos_produto (id_datos, id_producto, laboratorio_producto, ubicacion_producto, descripcion, lote, f_venc) values (26, 26, 'Nelco Laboratories, Inc.', '31 Dunning Place', '500 gr', '849172686-1', '17/1/2026');

select * from ordenPedido;
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (1, '5/12/2022', 2, 1, 1);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (2, '8/10/2022', 3, 2, 2);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (3, '7/2/2022', 3, 3, 3);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (4, '1/6/2023', 3, 4, 4);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (5, '4/5/2022', 1, 5, 5);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (6, '3/9/2023', 4, 6, 6);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (7, '12/1/2022', 4, 7, 7);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (8, '7/8/2022', 1, 8, 8);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (9, '5/11/2022', 4, 9, 9);
insert into ordenPedido (id_ordenPedido, fecha_pedido, id_tipo_pago, id_empleado, id_cliente) values (10, '1/4/2023', 1, 10, 10);


insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (1, 'Factura', '12/2/2022', 'aceptado', '10 d\EDas', 1);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (2, 'Boleta', '9/5/2022', 'aceptado', '0 d\EDas', 2);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (3, 'Boleta', '11/28/2022', 'aceptado', '5 d\EDas', 3);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (4, 'Factura', '10/24/2022', 'aceptado', '14 d\EDas', 4);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (5, 'Factura', '11/27/2022', 'aceptado', '12 d\EDas', 5);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (6, 'Boleta', '8/13/2022', 'aceptado', '5 d\EDas', 6);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (7, 'Factura', '10/7/2022', 'aceptado', '3 d\EDas', 7);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (8, 'Factura', '3/28/2023', 'aceptado', '8 d\EDas', 8);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (9, 'Boleta', '7/6/2022', 'aceptado', '21 d\EDas', 9);
insert into comprobante_pago (id_comprobante, tipo_comprobante, fecha_comprobante, condicion_pago, plazo_pago, id_ordenPedido) values (10, 'Boleta', '3/8/2023', 'aceptado', '0 d\EDas', 10);

select * from detalle_comprobante;
insert into detalle_comprobante (id_comprobante, id_datos, p_unit, cantidad, descuento, subtotal, IGV, total) values (1, 1, 16.36, 5, 0, 1.5, 0.13, 18);
insert into detalle_comprobante (id_comprobante, id_datos, p_unit, cantidad, descuento, subtotal, IGV, total) values (2, 2, 4.20, 3, 0, 0.5, 0.13, 6);
insert into detalle_comprobante (id_comprobante, id_datos, p_unit, cantidad, descuento, subtotal, IGV, total) values (7, 7, 11.46, 4, 0, 6.2, 0.13, 13);
insert into detalle_comprobante (id_comprobante, id_datos, p_unit, cantidad, descuento, subtotal, IGV, total) values (10, 10, 14.30, 11, 0, 11.5, 0.13, 16);


