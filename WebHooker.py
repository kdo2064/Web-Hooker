import base64
import os
os.system("mkdir Hooked_site")
base64_program = "aW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCByZXF1ZXN0cwoKCmJsYWNrID0gIlwwMzNbMDszMG0iCnJlZCA9ICJcMDMzWzA7MzFtIgpicmVkID0gIlwwMzNbMTszMW0iCmdyZWVuID0gIlwwMzNbMDszMm0iCmJncmVlbiA9ICJcMDMzWzE7MzJtIgp5ZWxsb3cgPSAiXDAzM1swOzMzbSIKYnllbGxvdyA9ICJcMDMzWzE7MzNtIgpibHVlID0gIlwwMzNbMDszNG0iCmJibHVlID0gIlwwMzNbMTszNG0iCnB1cnBsZSA9ICJcMDMzWzA7MzVtIgpicHVycGxlID0gIlwwMzNbMTszNW0iCmN5YW4gPSAiXDAzM1swOzM2bSIKYmN5YW4gPSAiXDAzM1sxOzM2bSIKd2hpdGUgPSAiXDAzM1swOzM3bSIKbmMgPSAiXDAzM1swMG0iCgojIGxvZ29zCgpsb2dvID0gZiIiIgp7cmVkfeKWkuKWiOKWkeKWkeKWkuKWiCDilojiloDiloAg4paI4paA4paA4paEIOKWkeKWkSDilpLilojilpHilpLilogg4paI4paA4paA4paIIOKWiOKWgOKWgOKWiCDilojilpHilogg4paI4paA4paAIOKWiOKWgOKWgOKWiCAKe3B1cnBsZX3ilpLilojilpLilojilpLilogg4paI4paA4paAIOKWiOKWgOKWgOKWhCDiloDiloAg4paS4paI4paA4paA4paIIOKWiOKWkeKWkeKWiCDilojilpHilpHilogg4paI4paA4paEIOKWiOKWgOKWgCDilojiloTiloTiloAgCntjeWFufeKWkuKWiOKWhOKWgOKWhOKWiCDiloDiloDiloAg4paA4paA4paA4paRIOKWkeKWkSDilpLilojilpHilpLilogg4paA4paA4paA4paAIOKWgOKWgOKWgOKWgCDiloDilpHiloAg4paA4paA4paAIOKWgOKWkeKWgOKWgAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHtyZWR9W3tibHVlfVZ7Z3JlZW59MS4we3JlZH1dCgoiIiIKbWFpbm1lbnUgPSBmIiIiCntyZWR9X19fX19fX19fX19fX19fX19fX19fCnx7d2hpdGV9LS0tLXtiY3lhbn1DeWJlci1EIEFybXl7d2hpdGV9LS0tLXtyZWR9fAp8ICAgICAgICAgICAgICAgICAgICB7cmVkfXwKfHt3aGl0ZX0te3JlZH14e3doaXRlfS17cmVkfVt7Z3JlZW59MXtyZWR9XXt3aGl0ZX0te3llbGxvd30+e2dyZWVufVNpdGVze3JlZH0gICAgICAgfAp8e3doaXRlfS17cmVkfXh7d2hpdGV9LXtyZWR9W3tncmVlbn0ye3JlZH1de3doaXRlfS17eWVsbG93fT57Z3JlZW59VW5pbnRhbGx7cmVkfSAgICB8Cnx7d2hpdGV9LXtyZWR9eHt3aGl0ZX0te3JlZH1be2dyZWVufTN7cmVkfV17d2hpdGV9LXt5ZWxsb3d9PntncmVlbn1VcGRhdGV7cmVkfSAgICAgIHwKfHt3aGl0ZX0te3JlZH14e3doaXRlfS17cmVkfVt7Z3JlZW59NHtyZWR9XXt3aGl0ZX0te3llbGxvd30+e2dyZWVufUFib3V0IHtyZWR9ICAgICAgfAp8e3doaXRlfS17cmVkfXh7d2hpdGV9LXtyZWR9W3tncmVlbn01e3JlZH1de3doaXRlfS17eWVsbG93fT57Z3JlZW59RXhpdCB7cmVkfSAgICAgICB8CnxfX19fX19fX19fX19fX19fX19fX3wKCiIiIgoKCmRlZiBhYm91dCgpOgogICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICBwcmludChsb2dvKQogICAgcHJpbnQoZiIiIgp7YmN5YW59Wy1dVGhpcyB0b29sIGlzIENyZWF0ZWQgQnkgQ3liZXItRCBBcm15Cgp7eWVsbG93fUF1dGhvciAgICA6ICBLLkQuTwpHaXRodWIgICAgOiAgaHR0cHM6Ly9naXRodWIuY29tL2tkbzIwNjQKVGVsZWdyYW0gIDogIGh0dHBzOi8vdC5tZS9jeWJlcmRvZmZmaWNpYWwKRGlzY29yZCAgIDogIGh0dHBzOi8vZGlzY29yZC5nZy92OEZWenN1SApWZXJzaW9uICAgOiAgMS4wCgp7cmVkfVstXVdhcm5pbmc6Cgp7Ymx1ZX1UaGlzIFRvb2wgaXMgbWFkZSBmb3IgZWR1Y2F0aW9uYWwgcHVycG9zZQpvbmx5ICEgQXV0aG9yIHdpbGwgbm90IGJlIHJlc3BvbnNpYmxlIGZvcgphbnkgbWlzdXNlIG9mIHRoaXMgdG9vbCAhCgp7YnB1cnBsZX1bLV1BYm91dCBVcGRhdGU6Cgp7YnJlZH1Db21pbmcgc29vbi4uIQoKe2JncmVlbn1bLV1EZXYgU29jaWFsTWVkaWEKCntyZWR9W3tieWVsbG93fTF7cmVkfV17d2hpdGV9LXtyZWR9PntiY3lhbn1LLkQuTyAgIDogSW5zdGFncmFtCntyZWR9W3tieWVsbG93fTB7cmVkfV17d2hpdGV9LXtyZWR9PntiY3lhbn1FeGl0CiIiIikKICAgIGFzayA9IGlucHV0KGYie3llbGxvd31DaG9vc2UgYW4gT3B0aW9uOntncmVlbn0iKQogICAgaWYgYXNrID09ICIxIjoKICAgICAgICBvcy5zeXN0ZW0oCiAgICAgICAgICAgICJ4ZGctb3BlbiBodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL2N5YmVyX2Rfa2RvLyA+IC9kZXYvbnVsbCAyPiYxICYiKQogICAgZWxpZiBhc2sgPT0gIjIiOgogICAgICAgIG9zLnN5c3RlbSgicHl0aG9uMyBXZWJIb29rZXIucHkiKQogICAgZWxzZToKICAgICAgICBwcmludChmIntyZWR9SW52YWxpZWQgT3B0aW9uLi4uISIpCiAgICAgICAgdGltZS5zbGVlcCgwLjkpCiAgICAgICAgYWJvdXQoKQoKCiMgYWdhaW4gc3RhcnQKCmRlZiBzdGFydGFnYWluKCk6CiAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgIHByaW50KGxvZ28pCiAgICBwcmludChmIntyZWR9Q2hlY2sgSG9va2VkX1NpdGUgZm9sZGVyLi4uIikKICAgIGJhY2s9aW5wdXQoZiJ7eWVsbG93fURvIHlvdSB3YW50IHRvIHJ1biBhZ2FpbiBbeS9uXTp7Z3JlZW59IikKICAgIGlmIGJhY2s9PSJ5IiBvciBiYWNrPT0iWSI6CiAgICAgICAgb3Muc3lzdGVtKCJweXRob24zIFdlYkhvb2tlci5weSIpCiAgICBlbGlmIGJhY2sgPT0gIk4iIG9yIGJhY2sgPT0ibiI6CiAgICAgICAgb3Muc3lzdGVtKCJleGl0IikKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoZiJJbnZhaWxlZCBvcHRpb24uLi4iKQogICAgICAgIHRpbWUuc2xlZXAoMSkKICAgICAgICBzdGFydGFnYWluKCkKCiMgbG9nbyBlbmQKCiMgbG9naWMKZGVmIG1haW5sb2dpYygpOgogICAgYXNrID0gaW5wdXQoZiJ7eWVsbG93fUNob29zZSBhbiBPcHRpb246e2dyZWVufSIpCiAgICBpZiBhc2sgPT0gIjEiOgogICAgICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgICAgIHByaW50KGxvZ28pCiAgICAgICAgd2Vic2l0ZSA9IGlucHV0KGYie3llbGxvd31TaXRlIFVybDp7Z3JlZW59IikKICAgICAgICBwcmludChmIntncmVlbn1Eb3dubG9hZGluZy4uLi4iKQogICAgICAgIG9zLnN5c3RlbSgiY2xlYXIiKQogICAgICAgIHByaW50KGxvZ28pCiAgICAgICAgb3Muc3lzdGVtKCJjZCBIb29rZWRfc2l0ZSAmJiB3Z2V0IC0tbGltaXQtcmF0ZT0yMDBrIC0tbm8tY2xvYmJlciAtLWNsb2JiZXIgLS1jb252ZXJ0LWxpbmtzIC0tcmFuZG9tLXdhaXQgLXIgLXAgLUUgLWUgcm9ib3RzPW9mZiAtVSBtb3ppbGxhICIrd2Vic2l0ZSkKICAgICAgICBzdGFydGFnYWluKCkKICAgICAgICAKICAgIGVsaWYgYXNrID09ICIyIjoKICAgICAgICBvcy5zeXN0ZW0oImNkIC4uICYmIHJtIC1yZiBXZWItSG9va2VyICYmIHJtIC1yZiBIb29rZWRfc2l0ZSIpCiAgICBlbGlmIGFzayA9PSAiMyI6CiAgICAgICAgb3Muc3lzdGVtKCJjZCAuLiAmJiBybSAtcmYgV2ViLUhvb2tlciAgJiYgZ2l0IGNsb25lICBodHRwczovL2dpdGh1Yi5jb20va2RvMjA2NC9XZWItSG9va2VyICYmIGNkIFdlYi1Ib29rZXIgJiYgcHl0aG9uMyBzZXR1cC5weSIpCiAgICBlbGlmIGFzayA9PSAiNCI6CiAgICAgICAgYWJvdXQoKQogICAgZWxpZiBhc2sgPT0gIjUiOgogICAgICAgIG9zLnN5c3RlbSgiZXhpdCIpCiAgICBlbHNlOgogICAgICAgIHByaW50KGYie3JlZH1JbnZhbGllZCBPcHRpb24uLi4hIikKICAgICAgICB0aW1lLnNsZWVwKDAuOSkKICAgICAgICBvcy5zeXN0ZW0oInB5dGhvbjMgV2ViSG9va2VyLnB5IikKCgojIG1haW4gY29kZQpvcy5zeXN0ZW0oImNsZWFyIikKcHJpbnQobG9nbykKcHJpbnQoZiJ7Z3JlZW59Wy1dQ2hlY2tpbmcgSW50ZXJuZXQgQ29ubmVjdGlvbi4uLiIpCgp0cnk6CiAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCgiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbSIpCiAgICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSAyMDA6CiAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgICAgcHJpbnQobG9nbykKICAgICAgICBwcmludChmIntncmVlbn1bLV1Db25uZWN0ZWQuLi4gIikKICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICAgICAgb3Muc3lzdGVtKCJjbGVhciIpCiAgICAgICAgcHJpbnQobG9nbykKICAgICAgICBwcmludChtYWlubWVudSkKICAgICAgICBtYWlubG9naWMoKQoKCmV4Y2VwdCBFeGNlcHRpb246CiAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgIHByaW50KGxvZ28pCiAgICBwcmludChmIiIie3JlZH1bLV1DaGVjayBZb3VyIEludGVybmV0IENvbm5lY3Rpb24uLmFuZCBUcnkgQWdhaW4iIiIpCg=="
decoded_program = base64.b64decode(base64_program).decode()
exec(decoded_program)