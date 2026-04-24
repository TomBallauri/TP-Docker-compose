db = db.getSiblingDB('blog_db');

db.posts.insertMany([
    { title: "Premier article", content: "Contenu du premier article", author: "Alice", createdAt: new Date() },
    { title: "Deuxième article", content: "Contenu du deuxième article", author: "Bob", createdAt: new Date() },
    { title: "Troisième article", content: "Contenu du troisième article", author: "Charlie", createdAt: new Date() },
    { title: "Quatrième article", content: "Contenu du quatrième article", author: "Diana", createdAt: new Date() },
    { title: "Cinquième article", content: "Contenu du cinquième article", author: "Eve", createdAt: new Date() }
]);
