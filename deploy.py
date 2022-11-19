print('deploying...')

import subprocess
#./node_modules/.bin/truffle deploy --development

subprocess.call(["npx","truffle","deploy --development"])