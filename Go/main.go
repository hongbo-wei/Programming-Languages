package main

import "fmt"

// Create the function fuelGauge() here
func fuelGauge(fuel int) {
  fmt.Println("Fuel left:", fuel)
}

// Create the function calculateFuel() here
func calculateFuel(planet string) int {
  var fuel int
  switch planet {
    case "Venus":
      fuel = 300000
    case "Mercury":
      fuel = 500000
    case "Mars":
      fuel = 700000
    default:
      fuel = 0
  }
  return fuel
}

// Create the function greetPlanet() here
func greetPlanet(planet string) {
  fmt.Printf("Welcome, you are heading towards %s!\n", planet)
}

// Create the function cantFly() here
func cantFly() {
  fmt.Println("We do not have the available fuel to fly there.")
}

// Create the function flyToPlanet() here
func flyToPlanet(planet string, fuel int) int {
  var fuelRemaining, fuelCost int
  fuelRemaining = fuel
  fuelCost = calculateFuel(planet)

  if fuelRemaining >= fuelCost {
    greetPlanet(planet)
    fuelRemaining -= fuelCost
  } else {
    cantFly()
  }
  return fuelRemaining
}

// Returns your spaceship back to your home planet
func returnToHomePlanet(currentPlanet string, fuel int) int {
  defer greetPlanet("earth")
  var fuelCost int
  switch currentPlanet {
    case "Venus":
      fuelCost = 300000
    case "Mercury":
      fuelCost = 500000
    case "Mars":
      fuelCost = 700000
    default:
      fuelCost = 0
  }
  fuel -= fuelCost
  return fuel
}

func main() {
  // Create `planetChoice` and `fuel`
  var fuel int
  fuel = 1000000

  var planetChoice string
  planetChoice = "Venus"
  // And then liftoff!
  fuel = flyToPlanet(planetChoice, fuel)
  fuelGauge(fuel)

  fuelGauge(returnToHomePlanet(planetChoice,fuel))
}