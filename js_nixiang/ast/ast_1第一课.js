const {parse} = require('@babel/parser');               // 将js转换成ast
const generator = require('@babel/generator').default;  // 将ast转换为js的语法
const traverse = require('@babel/traverse');            // 节点遍历操作的方便功能
const types = require('@babel/types');                  // 提供一个与格式相关的对象合集，可以操作从而生成节点
const ast_code = parse('var a; a = "yuanrenxue"');
console.log('修改前', ast_code.program.body[0].declarations[0].id.name);
console.log('修改前', ast_code.program.body[1].expression.right.value);

ast_code.program.body[0].declarations[0].id.name = 'b';
ast_code.program.body[1].expression.left.name = 'b';
ast_code.program.body[1].expression.right.value = 'b-yuanrenxue';
console.log(ast_code.program.body[0].declarations[0].id.name);
console.log(ast_code.program.body[1].expression.left.name);
console.log(ast_code.program.body[1].expression.right.value);

console.log('-------------------\nast转回js：\n',generator(ast_code).code);
