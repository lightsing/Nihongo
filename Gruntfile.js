/*global module:false*/
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' +
      '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
      '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
      '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
      ' Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %> */\n',
    // Task configuration.
    copy: {
      main: {
        files: [{
            expand: true,
            cwd: 'node_modules/abplayer-html5/build/css/',
            src: ['*'],
            dest: 'static/css/',
            filter: 'isFile'
          }, {
            expand: true,
            cwd: 'node_modules/abplayer-html5/build/js/',
            src: ['*'],
            dest: 'static/js/',
            filter: function(path) {
              path = path.split(/[\\/]/).splice(-1).pop();

              return !!(path.endsWith('js') && !path.startsWith('jquery'));
          }}
        ]
      }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-contrib-copy');
  // Default task.
  grunt.registerTask('default', ['copy']);

};
