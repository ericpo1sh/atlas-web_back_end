import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof sqft !== 'number') {
      throw TypeError('Sqft must be a number');
    }
    if (typeof floors !== 'number') {
      throw TypeError('Floors must be a number');
    }
    this._sqft = sqft;
    this._floors = floors;
  }

  get sqft() {
    return self._sqft;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
