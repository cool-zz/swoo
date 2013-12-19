casper = require('casper').create({
    verbose: true,
    logLevel: 'debug',
    userAgent: 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
});

var site = casper.cli.get(0);

casper.start(site, function() {
    this.fill('form#postform', {
        'field4':    'LOOOOOOOOL BUMP.',
    }, true);

});

casper.then(function() {
   this.click('input[type="submit"]');

});

casper.run(function() {
    this.echo('message sent').exit();

});