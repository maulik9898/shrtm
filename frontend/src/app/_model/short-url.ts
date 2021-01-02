export class ShortUrl {
  constructor(
    // tslint:disable-next-line:variable-name
    public originalUrl: string,
    public slug?: string,
    public visits?: number,
    public createdAt?: Date

  ) {
  }
}
