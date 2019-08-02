import * as crypto from "crypto-js";

class MyBlock {
    public index: number;
    public prevHash: string;
    public hash: string;
    public data: string;
    public timestamp: number;

    static calculateSHA256 = (
        index: number,
        prevHash: string,
        data: string,
        timestamp: number
    ): string => crypto.SHA256(index + prevHash + data + timestamp).toString();

    static isValid = (candidateBlock: MyBlock, prevBlock: MyBlock): Boolean => {
        if (!(candidateBlock instanceof MyBlock)) {
            return false;
        } else if (candidateBlock.index !== prevBlock.index + 1) {
            return false;
        } else if (candidateBlock.prevHash !== prevBlock.hash) {
            return false;
        } else if (
            candidateBlock.hash !==
            MyBlock.calculateSHA256(
                candidateBlock.index,
                candidateBlock.prevHash,
                candidateBlock.data,
                candidateBlock.timestamp
            )
        ) {
            return false;
        } else {
            return true;
        }
    };

    constructor(
        index: number,
        prevHash: string,
        hash: string,
        data: string,
        timestamp: number
    ) {
        this.index = index;
        this.prevHash = prevHash;
        this.hash = hash;
        this.data = data;
        this.timestamp = timestamp;
    }
}

const getBlockChain = (): MyBlock[] => chain;

const getLatestBlock = (): MyBlock => chain[chain.length - 1];

const getNewTimestamp = (): number => Math.round(new Date().getTime() / 1000);

const addBlock = (block: MyBlock): void => {
    if (MyBlock.isValid(block, getLatestBlock())) {
        getBlockChain().push(block);
    }
};

const createNewBlock = (data: string): MyBlock => {
    const prevBlock = getLatestBlock();
    const newIndex: number = prevBlock.index + 1;
    const newTimestamp = getNewTimestamp();
    const newHash = MyBlock.calculateSHA256(
        newIndex,
        prevBlock.hash,
        data,
        newTimestamp
    );

    const newBlock: MyBlock = new MyBlock(
        newIndex,
        prevBlock.hash,
        newHash,
        data,
        newTimestamp
    );

    addBlock(newBlock);
    return newBlock;
};

const baseBlock: MyBlock = new MyBlock(0, "", "0123456780", "firstBlock", 0);

let chain: MyBlock[] = [baseBlock];
console.log("chain :", chain);

createNewBlock("first");
createNewBlock("second");
createNewBlock("third");
createNewBlock("fourth");

console.log("chain :", chain);
