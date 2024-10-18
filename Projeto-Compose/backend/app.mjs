import express from 'express';
import mongodb from 'mongodb';
import cors from 'cors';

const { MongoClient } = mongodb;

const app = express();
const port = 3000;
const mongoUrl = 'mongodb://database-mongo:27017';

app.use(cors());

app.get('/', (req, res) => {
    MongoClient.connect(mongoUrl, { useUnifiedTopology: true }, (err, client) => {
        if (err) {
            return res.status(500).send('Erro de conexão ao banco de dados');
        }
        res.send('Backend funcionando e conectado ao MongoDB!');
        client.close();
    });
});

app.listen(port, () => {
    console.log(`Backend rodando em http://localhost:${port}`);
});