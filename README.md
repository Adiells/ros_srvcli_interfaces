# Calc Service ROS 2

Simple project created to **practice** creating and using custom services in ROS 2 (Humble), with Python client and server nodes. Uses a custom `.srv` interface to perform basic math operations: addition, subtraction, multiplication, and division.

---

## Project Structure

- **calc_interfaces/**: package that defines the custom service interface `DoMath.srv`.
- **calc_service/**: package containing client and server nodes that use this interface.

---

## How to Use

1. Clone the repository and go to the workspace folder:

   ```bash
   cd ros2_ws
   ```

2. Build the workspace:

   ```bash
   colcon build
   source install/setup.bash
   ```

3. In terminal 1, run the server node:

   ```bash
   ros2 run calc_service service
   ```

4. In terminal 2, run the client node with parameters:

   ```bash
   ros2 run calc_service client <num1> <num2> <operation>
   ```

   Where:

   - `<num1>` and `<num2>` are integers.
   - `<operation>` can be: `soma`, `subtracao`, `multiplicacao`, or `divisao`.

---

## Example

```bash
ros2 run calc_service client 10 5 soma
```

Expected output:

```
Result: 15
Message: a soma de 10 + 5 = 15
```

---

## Technologies Used

- ROS 2 Humble
- Python 3
- `rclpy`
- Custom `.srv` service interface

---

## License

Apache License 2.0 — see LICENSE file for details.

---

Project made for study and practice, ideal for beginners learning custom services in ROS 2.
