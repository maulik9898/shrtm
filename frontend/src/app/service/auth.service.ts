import {Injectable, NgZone} from '@angular/core';
import {Router} from '@angular/router';

import {AngularFireAuth} from '@angular/fire/auth';
import firebase from 'firebase';
import auth = firebase.auth;
import {ShorturlService} from './shorturl.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  userData: any;
  idToken: string;
  isLogged: boolean;

 constructor(
    public afAuth: AngularFireAuth, // Inject Firebase auth service
    public router: Router,
    public ngZone: NgZone, // NgZone service to remove outside scope warning
    public shortUrlService: ShorturlService
  ) {
    /* Saving user data in localstorage when
    logged in and setting up null when logged out */
    this.afAuth.authState.subscribe(user => {
      if (user) {
        this.userData = user;
        this.isLogged = true;
        this.shortUrlService.getUser().subscribe(res => {});
        console.log('logged in');

      } else {
        this.userData = null;
        this.isLogged = false;
        console.log('Logged out');
      }
      this.router.navigate(['/']);
    });
    this.afAuth.onIdTokenChanged(user => {
      if (user){
        user.getIdToken().then(token => {
          this.idToken = token;
        });

      }else {
        this.idToken = null;
      }
    });

  }


  getToken(): string{
    return this.idToken;
  }

  // Sign in with email/password
  SignIn(email, password): any {
    return this.afAuth.signInWithEmailAndPassword(email, password)
      .then().catch((error) => {
        window.alert(error.message);
      });
  }

  // Sign up with email/password
  SignUp(email, password): any {
    return this.afAuth.createUserWithEmailAndPassword(email, password)
      .then((result) => {
        /* Call the SendVerificaitonMail() function when new user sign
        up and returns promise */
        console.log('Logged in');
      }).catch((error) => {
        window.alert(error.message);
      });
  }

  // Send email verfificaiton when new user sign up

  // Reset Forggot password
  ForgotPassword(passwordResetEmail): any {
    return this.afAuth.sendPasswordResetEmail(passwordResetEmail)
    .then(() => {
      window.alert('Password reset email sent, check your inbox.');
    }).catch((error) => {
      window.alert(error);
    });
  }

  // Returns true when user is looged in and email is verified
  get isLoggedIn(): boolean {
    return this.isLogged;
  }

  // Sign in with Google
  GoogleAuth(): any {
    return this.AuthLogin(new auth.GoogleAuthProvider());
  }

  // Auth logic to run auth providers
  AuthLogin(provider): any {
    return this.afAuth.signInWithPopup(provider)
    .then()
    .catch((error) => {
      window.alert(error);
    });
  }

  /* Setting up user data when sign in with username/password,
  sign up with username/password and sign in with social auth
  provider in Firestore database using AngularFirestore + AngularFirestoreDocument service */


  // Sign out
  SignOut(): any {
    return this.afAuth.signOut().then(() => {
      localStorage.removeItem('user');
    });
  }

}
