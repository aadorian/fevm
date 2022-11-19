print('migrate...')

import subprocess
#migrate --network live

subprocess.call(["npx","truffle","migrate --network live"])