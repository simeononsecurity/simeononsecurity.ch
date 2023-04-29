/*! THIS FILE IS AUTO-GENERATED */
import { AuthPlus } from 'googleapis-common';
import { publicca_v1alpha1 } from './v1alpha1';
import { publicca_v1beta1 } from './v1beta1';
export declare const VERSIONS: {
    v1alpha1: typeof publicca_v1alpha1.Publicca;
    v1beta1: typeof publicca_v1beta1.Publicca;
};
export declare function publicca(version: 'v1alpha1'): publicca_v1alpha1.Publicca;
export declare function publicca(options: publicca_v1alpha1.Options): publicca_v1alpha1.Publicca;
export declare function publicca(version: 'v1beta1'): publicca_v1beta1.Publicca;
export declare function publicca(options: publicca_v1beta1.Options): publicca_v1beta1.Publicca;
declare const auth: AuthPlus;
export { auth };
export { publicca_v1alpha1 };
export { publicca_v1beta1 };
export { AuthPlus, GlobalOptions, APIRequestContext, GoogleConfigurable, StreamMethodOptions, GaxiosPromise, MethodOptions, BodyResponseCallback, } from 'googleapis-common';
