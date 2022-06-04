from ncclient import manager
import webex
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

choice = ''

while choice != "8":
    print("List of device configurations: ")
    print("\n[1]-show running-config")
    print("[2]-create loopback interface")
    print("[3]-update interface description")
    print("[4]-create user")
    print("[5]-remove a user")
    print("[6]-delete an interface")
    print("[7]-send webex teams message")
    print("[8]-quit program")

    choice = input("\nEnter the option you want to do: ")

    if choice == "1":
        print("show running-config")
        running_config = m.get_config('running').xml
        print(xml.dom.minidom.parseString(running_config).toprettyxml())
        
    elif choice == "2":
        print("create a loopback interface")
        new_interface = """
        <config>
	        <native
		    xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		        <interface>
			        <Loopback>
				        <name>1</name>
				        <description>Kevin , Willord , Rejay</description>
				        <ip>
					        <address>
						        <primary>
							        <address>10.1.1.1</address>
							        <mask>255.255.255.0</mask>
						        </primary>
					        </address>
				        </ip>
			        </Loopback>
		        </interface>
	        </native>
        </config>
        """
        netconf_reply = m.edit_config(target="running", config=new_interface)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

    elif choice == "3":
        print("3-update interface description")
        loopback_int_description = """
        <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
            <interfaces xmlns="http://openconfig.net/yang/interfaces">
                <interface>
                    <name>GigabitEthernet1</name>
                        <config>
                            <description nc:operation="replace">Modified Interface Description</description>
                        </config>
                </interface>
            </interfaces>
        </config>
        """
        reply = m.edit_config(
            target="running",
            config=loopback_int_description,
            default_operation="none",
        )
        print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

    elif choice == "4":
        print("create user: ")
        cfg_name = input("enter username: ")
        cfg_password = input("enter password: ")
        create_username = """
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <username>
                    <name>test_user</name>
                    <privilege>15</privilege>
                    <password>
                        <encryption>0</encryption>
                        <password>cisco</password>
                    </password>
                </username>
            </native>
        </config>
        """
        reply = m.edit_config(
            target="running", config=create_username, default_operation="merge")
        print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

    elif choice == "5":
        print("remove a user")
        del_username = """
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <username operation="delete">
                    <name>test_user</name>
                </username>
            </native>
        </config>
        """
        reply = m.edit_config(
            target="running", config=del_username, default_operation="none")
        print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

    elif choice == "6":
        print("delete an interface")
        del_interface = """
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <Loopback operation="delete">
                        <name>1</name>
                    </Loopback>
                </interface>
            </native>
        </config>"""
        reply = m.edit_config(
            target="running", config=del_interface, default_operation="none")
        print(xml.dom.minidom.parseString(reply.xml).toprettyxml())

    elif choice == "7":
        print("Send webex teams message")
        webex.main()

    elif choice == "8":
        print("Program closing...")

    else:
        print("\nInvalid Input.Try again.")
