def estimate_cost(num_towers, fiber_length_km, cost_per_tower=12000, cost_per_km=600):
    return (num_towers * cost_per_tower) + (fiber_length_km * cost_per_km)
