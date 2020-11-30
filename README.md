# python-project-lvl3

<a href="https://codeclimate.com/github/LyuPo7/python-project-lvl3/maintainability"><img src="https://api.codeclimate.com/v1/badges/0f92f57e0c0e8d70281f/maintainability" /></a> <a href="https://codeclimate.com/github/LyuPo7/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/0f92f57e0c0e8d70281f/test_coverage" /></a> ![Python package](https://github.com/LyuPo7/python-project-lvl3/workflows/Python%20package/badge.svg)

<h3>Project Description:</h3>
    <p>HTML page loader utility</p>
    <ul>
        <li>Downloads any html page with resources to your local machine;</li>
        <li>Supports 4 levels of logging:
            <ul>
                <li><b>error</b>-level (default): show only error messages;</li>
                <li><b>warning</b>-level: show only error and warning messages;</li>
                <li><b>info</b>-level: show info messages for every step of downloading page including error and warning messages;</li>
                <li><b>debug</b>-level: show even more details than info-level;</li>
            </ul>
        </li>
    </ul>

<h3>Installation:</h3>
    <p>Download from PyPiTest:</p>
        <p><i>python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple lyupo7-page_loader</i></p>
    <a href="https://asciinema.org/a/374182" target="_blank"><img src="https://asciinema.org/a/374182.svg" /></a>

<h3>How to use?</h3>
    <p>Use <b>page-loader</b> command with appropriate keys.</p>
    <ul>
        <li> <h4>Usage without keys</h4>
            <p>Download html page to work directory</p>
            <a href="https://asciinema.org/a/374204" target="_blank"><img src="https://asciinema.org/a/374204.svg" /></a>
       </li>
        <li> <h4>Usage with output key</h4>
            <p>Download html page to directory in <b>output</b> key</p>
            <a href="https://asciinema.org/a/374207" target="_blank"><img src="https://asciinema.org/a/374207.svg" /></a>
       </li>
        <li> <h4>Usage with <b>verbosity</b> key</h4>
           <ul>
                <li> <p><b>Verbosity = error/warning</b></p>
                    <p>Show error/warning messages only if where was problems while downloading page</p>
                </li>
                <li> <p><b>Verbosity = info</b></p>
                    <p>Show info messages for every step of downloading page</p>
                    <a href="https://asciinema.org/a/374211" target="_blank"><img src="https://asciinema.org/a/374211.svg" /></a>
                </li>
                <li> <p><b>Verbosity = debug</b></p>
                    <p>Show debug messages about every step of downloading page</p>
                    <a href="https://asciinema.org/a/374212" target="_blank"><img src="https://asciinema.org/a/374212.svg" /></a>
                </li>
           </ul>
       </li>
    </ul>
