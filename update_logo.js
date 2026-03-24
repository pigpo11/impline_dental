const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const targetContent1 = `<div class="logo">임플라인치과 <span>| 포천점</span></div>`;
const replacement1 = `<a href="index.html" class="logo" style="text-decoration: none; color: inherit; cursor: pointer;">임플라인치과 <span>| 포천점</span></a>`;

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes(targetContent1)) {
        content = content.replace(targetContent1, replacement1);
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('Updated logo in ' + file);
    }
});
