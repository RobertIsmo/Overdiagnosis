'use strict';

//constants
const FACTOR_SIZE = 9;
const DISEASE_AMOUNT = 2;
const GEOGRAPHY_AMOUNT = 3
const TREATMENT_AMOUNT = 4;
const NOISE = 3;

const addNoise = () => {
	return Math.log(NOISE) * (2*Math.random() - 1)
}

const init = {
	diseaseSet: {
		diseaseA: [Object],
		diseaseB: [Object],
		diseaseC: [Object]
	},
	treatmentSet: {
		treatmentA: [Object],
		treatmentB: [Object],
		treatmentC: [Object],
		treatmentD: [Object],
	},
	geographicSet: {
		locationA: [Object],
		locationB: [Object]
	},
	professionalProfile: [Object]
}
const AgeBreakdown = () => {
	const obj = {
		a18_25: {relative:0, p:.27},
		a26_45: {relative:1, p:.43},
		a46_65: {relative:2, p:.30}
	}
	let count = 0;
	const keys = Object.keys(obj)
	for(let i = 0; i < keys.length; i++) {
		count += obj[keys[i]].p
	}
	console.assert(count === 1)
	return obj
}
const HealthBreakdown = () => {
	let factors = new Array(FACTOR_SIZE);
	for(let i = 0; i < factors.length; i++) {
		factors[i] = 1
	}
	return factors.slice()
}
const ScreeningBreakdown = (numberofDiseases) => {
	let rates = new Array(numberofDiseases);
	for(let i = 0; i < rates.length; i++) {
		rates[i] = .1
	}
	return rates.slice()
}
const Geography = (age, health, screening, proportion) => {
	return {
		age,
		health,
		screening,
		proportion,
		diseaserates: new Array(DISEASE_AMOUNT)
	}
}

const Disease = () => {
	let factors = new Array(FACTOR_SIZE);
	for(let i = 0; i < factors.length; i++) {
		factors[i] = {a:1, b:0}
	}
	return {
		factors: factors.slice(),
		falsepos: .01,
		falseneg: .01
	}
}
const Treatment = () => {
	let factors = new Array(FACTOR_SIZE);
	for(let i = 0; i < factors.length; i++) {
		factors[i] = {a:1/1, b:0}
	}
	return {
		factors: factors.slice(),
		intensity: 3,
		applicationrate: .5
	}
}
const findProperTreatment = () => {
	//implement
}

const profile = {
	//screeningrate: [.23, .31],

}

const GenerateGeography = (amount) => {
	let geography = new Array(amount);
	for(let i = 0; i < geography.length; i++) {
		const age = AgeBreakdown();
		const health = HealthBreakdown();
		const screening = ScreeningBreakdown();
		const prop = 1/amount;
		geography[i] = Geography(age, health, screening, prop);
	}
	return geography
}
const GenerateDiseases = (amount) => {
	let diseases = new Array(amount);
	for(let i = 0; i < diseases.length; i++) {
		diseases[i] = Disease();
	}
	return diseases
}
const GenerateTreatments = (amount) => {
	let treatments = new Array(amount);
	for(let i = 0; i < treatments.length; i++) {
		treatments[i] = Treatment();
	}
	return treatments
}
const GenerateAfflictionRate = (disfactors, geofactors) => {
	let count = 0
	for(let i = 0; i < geofactors.length; i++) {
		const geofactor = geofactors[i]
		const a = disfactors[i].a
		const b = disfactors[i].b
		count += Math.tanh((Math.log(geofactor) + 2 + addNoise()) * (Math.tanh(a + b)))
	}
	return count / geofactors.length
}

const initial = {
	geography: GenerateGeography(GEOGRAPHY_AMOUNT),
	diseases: GenerateDiseases(DISEASE_AMOUNT),
	treatments: GenerateTreatments(TREATMENT_AMOUNT),
}

const AddAffliction = (initialconditions) => {
	for(let i = 0; i < initialconditions.geography.length; i++) {
		for (let j = 0; j < initialconditions.diseases.length; j++) {
			const dis = initialconditions.diseases[j].factors
			const geo = initialconditions.geography[i].health
			const rate = GenerateAfflictionRate(dis, geo)
			initialconditions.geography[i].diseaserates[j] = rate
		}
	}
}

const Step = (initialconditions, options) => {
	AddAffliction(initialconditions)

}

Step(initial)