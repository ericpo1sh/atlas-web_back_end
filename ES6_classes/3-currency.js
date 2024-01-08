export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    self._code = code;
    self._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code !== 'string') {
      throw TypeError('Code must be a string');
    } else {
      self._code = code;
    }
  }

  get name() {
    return this._name
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      self._name = name;
    }
  }

  displayFullCurrency(code, name) {
    return `${name} (${code})`;
  }
}
