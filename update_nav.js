const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const targetContent = `<li><a href="save-tooth.html">자연치아살리기</a></li>`;

const replacement = `<li>
                    <a href="save-tooth.html">자연치아살리기</a>
                    <ul class="dropdown">
                        <li><a href="cavity.html">충치치료</a></li>
                        <li><a href="nerve.html">신경치료</a></li>
                        <li><a href="scaling.html">스케일링</a></li>
                        <li><a href="gums.html">잇몸치료</a></li>
                    </ul>
                </li>`;

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    if (content.includes(targetContent)) {
        content = content.replace(targetContent, replacement);
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('Updated ' + file);
    }
});
