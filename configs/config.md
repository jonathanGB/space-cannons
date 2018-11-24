# Config

Format is a JSON array of objects. Each object describes a celestial body.

```
{
  "x": x-coordinate (in meters)
  "y": y-coordinate (in meters)
  "r": radius of the body (in meters)
  "m": mass of the body (in kg)
  "atmos": { // optional
    "p": density of the atmosphere (in kg/m^3)
    "h": height of the atmosphere (in meters)
  }
  "vx": x-component of the velocity of the body (in m/s)
  "vy": y-component of the velocity of the body (in m/s)
}
```