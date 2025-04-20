import speedtest

def speed_test():
    try:
        st = speedtest.Speedtest()

        # Fetch all available servers
        print("Fetching server list...")
        servers = st.get_servers()  # Fetch all servers

        # Create a list of servers
        server_list = []
        for server in servers.values():
            for s in server:
                server_list.append(s)

        # Display available servers 
        print("\nAvailable Servers:")
        for i, server in enumerate(server_list[:10]):  # Limit to top 10 servers
            print(f"{i+1}. {server['sponsor']} - {server['name']}, {server['country']}")

        # Ask user to select a server by number
        server_choice = int(input("\nSelect a server by number (1-10): ")) - 1
        if server_choice < 0 or server_choice >= len(server_list):
            print("Invalid selection. Please try again.")
            return

        # Get the selected server
        selected_server = server_list[server_choice]

        # Set the server manually
        st.get_servers([selected_server['id']])
        best = st.get_best_server()

        print(f"\nConnected to: {best['sponsor']} - {best['name']}, {best['country']}")
        print(f"Host: {best['host']}")
        print(f"Ping: {round(best['latency'], 2)} ms")

        # Perform the speed test
        print("\nTesting download speed...")
        download = round(st.download() / 1_000_000, 2)

        print("Testing upload speed...")
        upload = round(st.upload() / 1_000_000, 2)

        print("\n--- Speed Test Results ---")
        print(f"Download Speed: {download} Mbps")
        print(f"Upload Speed: {upload} Mbps")
        print(f"Ping: {round(st.results.ping, 2)} ms")

    except Exception as e:
        print("An error occurred during the speed test:")
        print(e)

speed_test()
