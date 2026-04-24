db = db.getSiblingDB('blog_db');

db.createCollection('posts', {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["title", "content", "author", "createdAt"],
            properties: {
                title: {
                    bsonType: "string",
                    description: "Le titre est obligatoire et doit être une chaîne"
                },
                content: {
                    bsonType: "string",
                    description: "Le contenu est obligatoire et doit être une chaîne"
                },
                author: {
                    bsonType: "string",
                    description: "L'auteur est obligatoire et doit être une chaîne"
                },
                createdAt: {
                    bsonType: "date",
                    description: "La date est obligatoire et doit être de type date"
                }
            }
        }
    },
    validationLevel: "strict",
    validationAction: "error"
});

db.posts.insertMany([
    { title: "Premier article",   content: "Contenu du premier article",   author: "Alice",   createdAt: new Date() },
    { title: "Deuxième article",  content: "Contenu du deuxième article",  author: "Bob",     createdAt: new Date() },
    { title: "Troisième article", content: "Contenu du troisième article", author: "Charlie", createdAt: new Date() },
    { title: "Quatrième article", content: "Contenu du quatrième article", author: "Diana",   createdAt: new Date() },
    { title: "Cinquième article", content: "Contenu du cinquième article", author: "Eve",     createdAt: new Date() }
]);
