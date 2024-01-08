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

  set sqft(sqft) {
    if (typeof sqft !== 'number') {
      throw TypeError('Sqft must be a number');
    } else {
      this._sqft = sqft;
    }
  }

  get floors() {
    return this._floors;
  }

  set floors(floors) {
    if (typeof floors !== 'number') {
      throw TypeError('Sqft must be a number');
    } else {
      this._floors = floors;
    }
  }

  evacuationWarningMessage() {
    return "Evacuate slowly the NUMBER_OF_FLOORS floors";
  }
}
