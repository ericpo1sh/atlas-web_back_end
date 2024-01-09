export default function guardrail(mathFunction) {
  const queue = [];
  let tryMathFunc;

  try {
    tryMathFunc = mathFunction;
  } catch (e) {
    tryMathFunc = `${e.name}: ${e.message}`;
  }

  queue.push(tryMathFunc);
  queue.push('Guardrail was processed');
  return queue;
}
