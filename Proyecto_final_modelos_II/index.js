//https://www.youtube.com/watch?v=ufdHsFClAk0

const Client = require('pg').Client
const client = new Client({
    user: "postgres",
    password: "contrasenia",
    host: "localhost",
    port: 5432,
    database: "BD_Juegos"
})

//usar()

//function usar() {
    client.connect()
        .then(() => console.log("Conexion Exitosa"))
        .then(() => client.query("INSERT INTO puntaje VALUES ($1,$2,$3)",[6,200,4]))
        .then(() => client.query("SELECT * FROM puntaje"))
        .then(results => console.table(results.rows))
        .catch(e => console.log(e))
        .finally(() => client.end())

//}