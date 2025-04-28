import os

out=open("out2.txt")
url='1'
while url!='':
      url = out.readline().replace('\n','')
      if url=='':
            break
      token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYi" \
          "fQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImNoYW5nd2FuZ2xvdTIwMSIsImV4cCI6MTc0MDk3MDAyMSwiaWF0IjoxNzM1Nzg2MDIxLCJpc3" \
          "MiOiJodHRwczovL3Vycy5lYXJ0aGRhdGEubmFzYS5nb3YiLCJpZGVudGl0eV9wcm92aWRlciI6ImVkbF9vcHMiLCJhY3IiOiJlZGwiLCJ" \
          "hc3N1cmFuY2VfbGV2ZWwiOjN9.NvgqSUswVRL6QgcCc_nCKujRhmM8q2NbQtJ667iEX8_JYRXKtRomxXlL47Q62a6el5OobU41KeZz31IF" \
          "ktOho0dzFPaQlVp3zhzSBqLynQtncOpGLiGweWJBAPQ1iITx8t83MvcQwWUhdJ3VQR3djT8kxQTwxc8FBWHcakXOKDj4S8FIebGKf7_oiN" \
          "UFCUO99bQ6OqRn0utZgxyPZppsq0Wme8pZfYl_sa5yE4-fuCvgcFGxWf9Fg1NiEm58JGZ6aCw6k_wFN3UruljXfX1KxYiolTObKDWYutYU" \
          "6yU765nKFm0jA4YhjrK9N_9XoNTLxWDD_vfnRA_lYqVjcWJZGg"
      commands = "wget -e robots=off -m -np -R .html,.tmp -nH --cut-dirs=3 \""+url+"\" --header \"Authorization: Bearer "+token+"\" -P ."
      print(commands)
      b=os.system(commands)
