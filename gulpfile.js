const gulp = require("gulp");
const ts = require("gulp-typescript");
const del = require("del");
const gulpUtil = require('gulp-util');
const tsProject = ts.createProject("tsconfig.json");

// deploy folder and folder name
const DEPLOY_PATH = {
    base_path: 'pttool_web/assets/',
    templates_path: 'pttool_web/templates/',
    compile_path: './pttool_web/assets/js/'
}

// static path
const STATIC = {
    html: './front-end/html/**',
    css: './front-end/css/**',
    img: './front-end/img/**',
    common: './front-end/common/**',
    js: './front-end/js/**'
}

// move html folder
gulp.task("html", () => {
    return gulp.src(STATIC.html)
        .pipe(gulp.dest(DEPLOY_PATH.templates_path));
});

// move css folder
gulp.task("css", () => {
    return gulp.src(STATIC.css)
        .pipe(gulp.dest(DEPLOY_PATH.base_path + 'css'));
});

// move img folder
gulp.task("img", () => {
    return gulp.src(STATIC.img)
        .pipe(gulp.dest(DEPLOY_PATH.base_path + 'img'));
});

// move common folder
gulp.task("common", () => {
    return gulp.src(STATIC.common)
        .pipe(gulp.dest(DEPLOY_PATH.base_path + 'common'));
});

// move js folder
gulp.task("js", () => {
    return gulp.src(STATIC.js)
        .pipe(gulp.dest(DEPLOY_PATH.base_path + 'js'));
});

// typescript compile
gulp.task("ts_compile", () => {
    return tsProject.src()
        .pipe(tsProject())
        .pipe(gulp.dest(DEPLOY_PATH.compile_path));
});

// watch change the static files
gulp.task('watcher', () => {
    let watcher = {
        css: gulp.watch(STATIC.css, ['css']),
        html: gulp.watch(STATIC.html, ['html']),
        img: gulp.watch(STATIC.img, ['img']),
        common: gulp.watch(STATIC.common, ['common']),
        js: gulp.watch(STATIC.js, ['js']),
        ts_compile: gulp.watch(tsProject.config['files'][0], ['ts_compile'])
    };
    let notify = (event) => {
        gulpUtil.log('File',
            gulpUtil.colors.yellow(event.path),
            'was',
            gulpUtil.colors.magenta(event.type))
    };
    for (let key in watcher) {
        watcher[key].on('change', notify);
    }
});

gulp.task('clean', function () {
    return del(DEPLOY_PATH.base_path, { force: true });
});

gulp.task("default", [
    "html",
    "css",
    "img",
    "common",
    "js"
], () => {});