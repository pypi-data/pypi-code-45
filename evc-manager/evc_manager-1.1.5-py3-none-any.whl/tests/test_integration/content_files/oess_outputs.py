""" Examples of circuit outputs provided by OESS to be used by other tests """


OESS_REPLY = {'remote_requester': None,
              'last_modified_by': {'status': 'active',
                                   'auth_id': '1',
                                   'family_name': 'API',
                                   'email': 'root@nobody',
                                   'is_admin': '0',
                                   'user_id': '1',
                                   'given_names': 'Dynamic',
                                   'type': 'normal',
                                   'auth_name': 'autoapi'},
              'external_identifier': None,
              'state': 'active',
              'backup_links': [{'interface_z': 'eth2/5',
                                'port_no_z': '53',
                                'node_z': 'Ampath1',
                                'port_no_a': '52',
                                'node_a': 'SouthernLight2',
                                'name': 'Atlantic',
                                'interface_z_id': '91',
                                'interface_a_id': '29491',
                                'interface_a': 'eth2/4'}],
              'remote_url': None,
              'created_on': '08/14/2018 16:45:06',
              'loop_node': None,
              'links': [{'interface_z': 'eth4/1',
                         'port_no_z': '145',
                         'node_z': 'Sax',
                         'port_no_a': '290',
                         'node_a': 'Ampath1',
                         'name': 'FTLZ-MIA-100G',
                         'interface_z_id': '29911',
                         'interface_a_id': '29741',
                         'interface_a': 'eth7/2'},
                        {'interface_z': 'eth4/2',
                         'port_no_z': '146',
                         'node_z': 'Sax',
                         'port_no_a': '241',
                         'node_a': 'SouthernLight2',
                         'name': 'FTLZ-SP-100G',
                         'interface_z_id': '29921',
                         'interface_a_id': '29771',
                         'interface_a': 'eth6/1'}],
              'circuit_id': '1000',
              'static_mac': '0',
              'workgroup_id': '1',
              'name': 'Dynamic-6655400c-9fe1-11e8-a349',
              'description': 'VLAN-1781-1781',
              'endpoints': [{'local': '1', 'node': 'SouthernLight2',
                             'mac_addrs': [],
                             'interface_description': 'OF Loop',
                             'port_no': '67',
                             'node_id': '3881', 'urn': None,
                             'interface': 'eth2/19', 'tag': '1781',
                             'role': 'unknown'},
                            {'local': '1', 'node': 'Ampath1',
                             'mac_addrs': [],
                             'interface_description': 'AtlanticWave-100G',
                             'port_no': '242',
                             'node_id': '11',
                             'urn': None, 'interface': 'eth6/2', 'tag': '1781',
                             'role': 'unknown'}],
              'workgroup': {'workgroup_id': '11', 'status': 'active',
                            'name': 'Dynamic',
                            'max_circuit_endpoints': '3',
                            'description': '', 'max_circuits': '50',
                            'external_id': None,
                            'type': 'normal', 'max_mac_address_per_end': '10'},
              'active_path': 'primary',
              'bandwidth': '0',
              'internal_ids': {'primary': {'SouthernLight2': {'29771': '1123'},
                                           'Sax': {'29911': '1123',
                                                   '29921': '1123'},
                                           'Ampath1': {'29741': '1123'}},
                               'backup': {'SouthernLight2': {'29491': '1101'},
                                          'Ampath1': {'91': '1101'}}},
              'last_edited': '08/31/2018 10:50:08',
              'user_id': '1',
              'restore_to_primary': '0',
              'operational_state': 'up',
              'created_by': {'status': 'active', 'auth_id': '1',
                             'family_name': 'Dynamic', 'email': 'root@nobody',
                             'is_admin': '0', 'user_id': '1',
                             'given_names': 'Dynamic', 'type': 'normal',
                             'auth_name': 'dynamic'},
             }


OESS_REPL2 = {'remote_requester': None,
              'last_modified_by': {'status': 'active', 'auth_id': '191',
                                   'family_name': 'API',
                                   'email': 'jab@amlight.net',
                                   'is_admin': '0',
                                   'user_id': '81',
                                   'given_names': 'Automation',
                                   'type': 'normal', 'auth_name': 'autoapi'},
              'external_identifier': None,
              'state': 'active',
              'backup_links': [{'interface_z': 'eth3/2',
                                'port_no_z': '98',
                                'node_z': 'AndesLight2',
                                'port_no_a': '98',
                                'node_a': 'AndesLight',
                                'name': 'AndesLight1-AndesLight2-100G',
                                'interface_z_id': '29941',
                                'interface_a_id': '29861',
                                'interface_a': 'eth3/2'},
                               {'interface_z': 'eth4/1',
                                'port_no_z': '145',
                                'node_z': 'Sax',
                                'port_no_a': '290',
                                'node_a': 'Ampath1',
                                'name': 'FTLZ-MIA-100G',
                                'interface_z_id': '29911',
                                'interface_a_id': '29741',
                                'interface_a': 'eth7/2'},
                               {'interface_z': 'eth4/2',
                                'port_no_z': '146',
                                'node_z': 'Sax',
                                'port_no_a': '241',
                                'node_a': 'SouthernLight2',
                                'name': 'FTLZ-SP-100G',
                                'interface_z_id': '29921',
                                'interface_a_id': '29771',
                                'interface_a': 'eth6/1'},
                               {'interface_z': 'eth2/1',
                                'port_no_z': '49',
                                'node_z': 'AndesLight2',
                                'port_no_a': '53',
                                'node_a': 'Ampath2',
                                'name': 'Pacific',
                                'interface_z_id': '311',
                                'interface_a_id': '51',
                                'interface_a': 'eth2/5'},
                               {'interface_z': 'eth3/1',
                                'port_no_z': '97',
                                'node_z': 'AndesLight',
                                'port_no_a': '289',
                                'node_a': 'SouthernLight2',
                                'name': 'Terrestrial-100G',
                                'interface_z_id': '29871',
                                'interface_a_id': '29791',
                                'interface_a': 'eth7/1'}],
              'remote_url': None,
              'created_on': '03/29/2016 00:06:40',
              'loop_node': None,
              'links': [{'interface_z': 'eth7/1',
                         'port_no_z': '289',
                         'node_z': 'Ampath2',
                         'port_no_a': '289',
                         'node_a': 'Ampath1',
                         'name': 'Ampath1-Ampath2-100G',
                         'interface_z_id': '29711',
                         'interface_a_id': '29721',
                         'interface_a': 'eth7/1'},
                        {'interface_z': 'eth4/1',
                         'port_no_z': '145',
                         'node_z': 'Sax',
                         'port_no_a': '290',
                         'node_a': 'Ampath1',
                         'name': 'FTLZ-MIA-100G',
                         'interface_z_id': '29911',
                         'interface_a_id': '29741',
                         'interface_a': 'eth7/2'},
                        {'interface_z': 'eth4/2',
                         'port_no_z': '146',
                         'node_z': 'Sax',
                         'port_no_a': '241',
                         'node_a': 'SouthernLight2',
                         'name': 'FTLZ-SP-100G',
                         'interface_z_id': '29921',
                         'interface_a_id': '29771',
                         'interface_a': 'eth6/1'},
                        {'interface_z': 'eth3/1',
                         'port_no_z': '97',
                         'node_z': 'AndesLight',
                         'port_no_a': '289',
                         'node_a': 'SouthernLight2',
                         'name': 'Terrestrial-100G',
                         'interface_z_id': '29871',
                         'interface_a_id': '29791',
                         'interface_a': 'eth7/1'}],
              'circuit_id': '711', 'static_mac': '1', 'workgroup_id': '1',
              'name': 'AmLight-1d1e9fce-f542-11e5-9a7f-000c29e0ca3f',
              'description': 'Vlan_4001_AmLight',
              'endpoints': [{'local': '1', 'node': 'Ampath1',
                             'mac_addrs': [{
                                 'mac_address': 'c8:1f:66:cb:b6:3c'}],
                             'interface_description': 'AtlanticWave-10G',
                             'port_no': '56', 'node_id': '11', 'urn': None,
                             'interface': 'eth2/8', 'tag': '495',
                             'role': 'unknown'},
                            {'local': '1', 'node': 'AndesLight',
                             'mac_addrs': [{
                                 'mac_address': 'a0:36:9f:4d:d7:7c'}],
                             'interface_description': 'perfSonar|10G|p2p1',
                             'port_no': '56', 'node_id': '21', 'urn': None,
                             'interface': 'eth2/8', 'tag': '4001',
                             'role': 'unknown'},
                            {'local': '1', 'node': 'SouthernLight2',
                             'mac_addrs': [{
                                 'mac_address': '90:e2:ba:2c:45:9d'}],
                             'interface_description': 'perfSonar-OWAMP',
                             'port_no': '59', 'node_id': '3881', 'urn': None,
                             'interface': 'eth2/11', 'tag': '4001',
                             'role': 'unknown'},
                            {'local': '1', 'node': 'Ampath2',
                             'mac_addrs': [{
                                 'mac_address': '78:45:c4:f0:c9:dc'}],
                             'interface_description': 'Brocade ICX',
                             'port_no': '52', 'node_id': '1', 'urn': None,
                             'interface': 'eth2/4', 'tag': '4001',
                             'role': 'unknown'},
                            {'local': '1', 'node': 'Ampath2',
                             'mac_addrs': [{
                                 'mac_address': '2c:6b:f5:ab:8f:c0'}],
                             'interface_description': 'Translation Loop',
                             'port_no': '56', 'node_id': '1', 'urn': None,
                             'interface': 'eth2/8', 'tag': '4001',
                             'role': 'unknown'}],
              'workgroup': {'workgroup_id': '1', 'status': 'active',
                            'name': 'AmLight', 'max_circuit_endpoints': '10',
                            'description': '', 'max_circuits': '2000',
                            'external_id': None, 'type': 'admin',
                            'max_mac_address_per_end': '100'},
              'active_path': 'primary',
              'bandwidth': '0',
              'internal_ids': {
                  'primary': {'SouthernLight2': {'29771': '1111',
                                                 '29791': '1102'},
                              'Ampath2': {'29711': '1101'},
                              'Sax': {'29911': '1121', '29921': '1121'},
                              'AndesLight': {'29871': '1102'},
                              'Ampath1': {'29741': '1111', '29721': '1101'}},
                  'backup': {'SouthernLight2': {'29771': '1132',
                                                '29791': '1107'},
                             'AndesLight2': {'29941': '1102', '311': '1139'},
                             'Ampath2': {'51': '1139'},
                             'Sax': {'29911': '1132', '29921': '1132'},
                             'AndesLight': {'29871': '1107', '29861': '1102'},
                             'Ampath1': {'29741': '1132'}}},
              'last_edited': '06/26/2018 00:21:19',
              'user_id': '81',
              'restore_to_primary': '2',
              'operational_state': 'up',
              'created_by': {'status': 'active', 'auth_id': '171',
                             'family_name': 'Admin', 'email': 'root@nobody',
                             'is_admin': '0', 'user_id': '11',
                             'given_names': 'AmLight', 'type': 'normal',
                             'auth_name': 'amlight'}
             }

OESS_REPL3 = {'remote_requester': None,
              'last_modified_by': {'status': 'active',
                                   'auth_id': '1',
                                   'family_name': 'API',
                                   'email': 'root@nobody',
                                   'is_admin': '0',
                                   'user_id': '1',
                                   'given_names': 'Dynamic',
                                   'type': 'normal',
                                   'auth_name': 'autoapi'},
              'external_identifier': None,
              'state': 'active',
              'backup_links': [],
              'remote_url': None,
              'created_on': '08/14/2018 16:45:06',
              'loop_node': None,
              'links': [],
              'circuit_id': '1000',
              'static_mac': '0',
              'workgroup_id': '1',
              'name': 'Dynamic-6655400c-9fe1-11e8-a349',
              'description': 'VLAN-TESTE',
              'endpoints': [{'local': '1', 'node': 'SouthernLight2',
                             'mac_addrs': [],
                             'interface_description': 'OF Loop',
                             'port_no': '67',
                             'node_id': '3881', 'urn': None,
                             'interface': 'eth2/19', 'tag': '1781',
                             'role': 'unknown'},
                            {'local': '1', 'node': 'Ampath1',
                             'mac_addrs': [],
                             'interface_description': 'AtlanticWave-100G',
                             'port_no': '242',
                             'node_id': '11',
                             'urn': None, 'interface': 'eth6/2', 'tag': '1781',
                             'role': 'unknown'}],
              'workgroup': {'workgroup_id': '11', 'status': 'active',
                            'name': 'Dynamic',
                            'max_circuit_endpoints': '3',
                            'description': '', 'max_circuits': '50',
                            'external_id': None,
                            'type': 'normal', 'max_mac_address_per_end': '10'},
              'active_path': 'primary',
              'bandwidth': '0',
              'internal_ids': {'primary': {'SouthernLight2': {'29771': '1123'},
                                           'Sax': {'29911': '1123',
                                                   '29921': '1123'},
                                           'Ampath1': {'29741': '1123'}},
                               'backup': {'SouthernLight2': {'29491': '1101'},
                                          'Ampath1': {'91': '1101'}}},
              'last_edited': '08/31/2018 10:50:08',
              'user_id': '1',
              'restore_to_primary': '0',
              'operational_state': 'up',
              'created_by': {'status': 'active', 'auth_id': '1',
                             'family_name': 'Dynamic', 'email': 'root@nobody',
                             'is_admin': '0', 'user_id': '1',
                             'given_names': 'Dynamic', 'type': 'normal',
                             'auth_name': 'dynamic'},
             }

OESS_REPL4 = {'remote_requester': None,
              'last_modified_by': {'status': 'active',
                                   'auth_id': '1',
                                   'family_name': 'API',
                                   'email': 'root@nobody',
                                   'is_admin': '0',
                                   'user_id': '1',
                                   'given_names': 'Dynamic',
                                   'type': 'normal',
                                   'auth_name': 'autoapi'},
              'external_identifier': None,
              'state': 'active',
              'backup_links': [],
              'remote_url': None,
              'created_on': '08/14/2018 16:45:06',
              'loop_node': None,
              'links': [],
              'circuit_id': '1000',
              'static_mac': '0',
              'workgroup_id': '1',
              'name': 'Dynamic-6655400c-9fe1-11e8-a349',
              'description': 'VLAN-TESTE2',
              'endpoints': [{'local': '1', 'node': 'SouthernLight2',
                             'mac_addrs': [],
                             'interface_description': 'OF Loop',
                             'port_no': '67', 'node_id': '3881',
                             'urn': None,
                             'interface': 'eth2/19', 'tag': '1781', 'role': 'unknown'},
                            {'local': '1', 'node': 'Ampath1',
                             'mac_addrs': [],
                             'interface_description': 'AtlanticWave-100G',
                             'port_no': '242', 'node_id': '11',
                             'urn': None,
                             'interface': 'eth6/2', 'tag': '1781', 'role': 'unknown'}],
              'workgroup': {'workgroup_id': '11',
                            'status': 'active',
                            'name': 'Dynamic',
                            'max_circuit_endpoints': '3',
                            'description': '', 'max_circuits': '50',
                            'external_id': None,
                            'type': 'normal', 'max_mac_address_per_end': '10'},
              'active_path': 'primary',
              'bandwidth': '0',
              'internal_ids': {'primary': {'SouthernLight2': {'29771': '1123'},
                                           'Sax': {'29911': '1123', '29921': '1123'},
                                           'Ampath1': {'29741': '1123'}},
                               'backup': {'SouthernLight2': {'29491': '1101'},
                                          'Ampath1': {'91': '1101'}}},
              'last_edited': '08/31/2018 10:50:08',
              'user_id': '1',
              'restore_to_primary': '0',
              'operational_state': 'up',
              'created_by': {'status': 'active', 'auth_id': '1',
                             'family_name': 'Dynamic', 'email': 'root@nobody',
                             'is_admin': '0', 'user_id': '1',
                             'given_names': 'Dynamic', 'type': 'normal',
                             'auth_name': 'dynamic'}
              }
